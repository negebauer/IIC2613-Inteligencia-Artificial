from s3_1 import run

train = 'TrainSet'
test = 'TestSet'

if __name__ == '__main__':
    run(train, test, 's3_1_s_1to100inc1.log', 1, 101, 1)
