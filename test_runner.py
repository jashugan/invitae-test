from unittest import TextTestRunner, TestLoader
import test_acceptance
import test_merger

if __name__ == '__main__':

    # load tests
    test_loader = TestLoader()
    suite = test_loader.loadTestsFromModule(test_acceptance)
    suite.addTest(test_loader.loadTestsFromModule(test_merger))

    # run suite
    TextTestRunner().run(suite)