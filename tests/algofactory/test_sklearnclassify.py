#test relation extration
#author shimin

from chi_annotator.algo_factory.components import ComponentBuilder
from chi_annotator.algo_factory.common import Message
from chi_annotator.task_center.config import AnnotatorConfig
from chi_annotator.algo_factory.common import TrainingData

class TestClassify(object):
    self.pos_msg1 = Message(u"你好，我是一个demo!!!!", {"label": "good"})
    self.pos_msg2 = Message(u"你好,你好,你好", {"label": "good"})
    self.pos_msg3 = Message(u"好的呀，不错", {"label": "good"})
    self.neg_msg1 = Message(u"如果发现有文件漏提或注释有误", {"label": "bad"})
    self.neg_msg2 = Message(u"增加一个需要上传的文件", {"label": "bad"})
    self.neg_msg3 = Message(u"有一个上传的文件", {"label": "bad"})
    def test_svm_classify(self):
        cfg = AnnotatorConfig()
        train_data = TrainingData([neg_msg1, neg_msg2, pos_msg1, pos_msg2])
        cb = ComponentBuilder()
        char_tokenize = cb.create_component("char_tokenizer", cfg)
        sent_embedding = cb.create_component("sentence_embedding_extractor", cfg)
        svm_classifer = cb.create_component("SVM_classifier", cfg)
        char_tokenize.train(train_data, cfg)
        sent_embedding.train(train_data, cfg)
        svm_classifer.train(train_data, cfg)
        # test
        test_msg = Message(u"增加一个需要上传的文件")
        char_tokenize.process(test_msg, **{})
        sent_embedding.process(test_msg, **{})
        svm_classifer.process(test_msg, **{})

        assert test_msg.get("classifylabel").get("name") == "bad"
    def test_sgd_classify(self):
        cfg = AnnotatorConfig()
        train_data = TrainingData([neg_msg1, neg_msg2, pos_msg1, pos_msg2])
        cb = ComponentBuilder()
        char_tokenize = cb.create_component("char_tokenizer", cfg)
        sent_embedding = cb.create_component("sentence_embedding_extractor", cfg)
        SGD_Classifier = cb.create_component("SGD_Classifier", cfg)
        char_tokenize.train(train_data, cfg)
        sent_embedding.train(train_data, cfg)
        SGD_Classifier.train(train_data, cfg)
        # test
        test_msg = Message(u"增加一个需要上传的文件")
        char_tokenize.process(test_msg, **{})
        sent_embedding.process(test_msg, **{})
        SGD_Classifier.process(test_msg, **{})

        assert test_msg.get("classifylabel").get("name") == "bad"
    def test_knn_classify(self):
        cfg = AnnotatorConfig()
        train_data = TrainingData([neg_msg1, neg_msg2, neg_msg3, pos_msg1, pos_msg2, pos_msg3])
        cb = ComponentBuilder()
        char_tokenize = cb.create_component("char_tokenizer", cfg)
        sent_embedding = cb.create_component("sentence_embedding_extractor", cfg)
        Knn_Classifier = cb.create_component("Knn_Classifier", cfg)
        char_tokenize.train(train_data, cfg)
        sent_embedding.train(train_data, cfg)
        Knn_Classifier.train(train_data, cfg)
        # test
        test_msg = Message(u"增加一个需要上传的文件")
        char_tokenize.process(test_msg, **{})
        sent_embedding.process(test_msg, **{})
        Knn_Classifier.process(test_msg, **{})

        assert test_msg.get("classifylabel").get("name") == "bad"
    def test_randomforest_classify(self):
        cfg = AnnotatorConfig()
        train_data = TrainingData([neg_msg1, neg_msg2, pos_msg1, pos_msg2])
        cb = ComponentBuilder()
        char_tokenize = cb.create_component("char_tokenizer", cfg)
        sent_embedding = cb.create_component("sentence_embedding_extractor", cfg)
        RandomForest_Classifier = cb.create_component("RandomForest_Classifier", cfg)
        char_tokenize.train(train_data, cfg)
        sent_embedding.train(train_data, cfg)
        RandomForest_Classifier.train(train_data, cfg)
        # test
        test_msg = Message(u"增加一个需要上传的文件")
        char_tokenize.process(test_msg, **{})
        sent_embedding.process(test_msg, **{})
        RandomForest_Classifier.process(test_msg, **{})

        assert test_msg.get("classifylabel").get("name") == "bad"
    def test_adaboost_classify(self):
        cfg = AnnotatorConfig()
        train_data = TrainingData([neg_msg1, neg_msg2, pos_msg1, pos_msg2])
        cb = ComponentBuilder()
        char_tokenize = cb.create_component("char_tokenizer", cfg)
        sent_embedding = cb.create_component("sentence_embedding_extractor", cfg)
        AdaBoost_Classifier = cb.create_component("AdaBoost_Classifier", cfg)
        char_tokenize.train(train_data, cfg)
        sent_embedding.train(train_data, cfg)
        AdaBoost_Classifier.train(train_data, cfg)
        # test
        test_msg = Message(u"增加一个需要上传的文件")
        char_tokenize.process(test_msg, **{})
        sent_embedding.process(test_msg, **{})
        AdaBoost_Classifier.process(test_msg, **{})

        assert test_msg.get("classifylabel").get("name") == "bad"
