#!/usr/bin/env python

from dotflow import DotFlow, action, retry



def callback(**kwargs):
    print(kwargs)


@action
@retry(max_retry=1)
def my_task():
    print("task")
    raise Exception("Task Error!")


def main():
    workflow = DotFlow()

    workflow.task.add(step=my_task, callback=callback)
    workflow.task.add(step=my_task, callback=callback)
    workflow.task.add(step=my_task)

    sequential = workflow.host.start(workflow=workflow).sequential(keep_going=True)
    background = workflow.host.start(workflow=workflow).background()
    parallel = workflow.host.start(workflow=workflow).parallel()
    data_store = workflow.host.start(workflow=workflow).data_store()


if __name__ == '__main__':
    main()