from s3_3 import run

train = 'TrainSet 2'
test = 'TestSet 2'

if __name__ == '__main__':
    run(train, test, 's3_3_b.log')
    run(train, train, 's3_3_b_trainvtrain.log')
