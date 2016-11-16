from s3_3 import run

train = 'TrainSet'
test = 'TestSet'

if __name__ == '__main__':
    run(train, test, 's3_3_s.log')
    run(train, train, 's3_3_s_trainvtrain.log')
