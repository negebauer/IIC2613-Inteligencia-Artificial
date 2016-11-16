from s3_2 import run

train = 'TrainSet'
test = 'TestSet'

if __name__ == '__main__':
    run(train, test, 's3_2_s.log')
    run(train, test, 's3_2_s_1000.log')
