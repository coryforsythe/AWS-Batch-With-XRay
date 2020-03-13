from aws_xray_sdk.core import xray_recorder # see https://github.com/aws/aws-xray-sdk-python

import time

xray_recorder.configure(
    sampling=True,
    context_missing='LOG_ERROR',
    plugins=('EC2Plugin', 'ECSPlugin'),
    daemon_address='127.0.0.1:2000',
)

@xray_recorder.capture('SubProcess1')
def subProcessOne():
    print("Running sub process 1")
    time.sleep(5)
    subProcessTwo()

@xray_recorder.capture('SubProcess2')
def subProcessTwo():
    print("Running sub process 2")
    if xray_recorder.is_sampled():
        xray_recorder.put_annotation('AnnotationKey', 'AnnotationValue')
        xray_recorder.put_metadata('MetadataKey', 'MetatDataValue')
    time.sleep(5)
    raise NameError('This is a NameError Exception')


with xray_recorder.in_segment('Batch_Processor') as segment:
    try:
        print('Starting Process')
        subProcessOne()

    except NameError:
        print('The excpected exception was raised')


