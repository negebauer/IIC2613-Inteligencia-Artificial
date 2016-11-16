from s3_2 import run

train = 'TrainSet 2'
test = 'TestSet 2'

if __name__ == '__main__':
    run(train, test, 's3_2_b.log')
    run(train, test, 's3_2_b_1000.log')
