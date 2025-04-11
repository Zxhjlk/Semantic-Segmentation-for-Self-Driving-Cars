import tensorflow as tf
import keras

#@keras.saving.register_keras_serializable()
class UpdatedMeanIoU(tf.keras.metrics.MeanIoU):
    def __init__(self,
               y_true=None,
               y_pred=None,
               num_classes=None,
               name=None,
               dtype=None,
               ignore_class=None,
               sparse_y_true=True,
               sparse_y_pred=True,
               axis=-1):
        super(UpdatedMeanIoU, self).__init__(num_classes = num_classes,name=name, dtype=dtype, ignore_class=ignore_class, sparse_y_true=sparse_y_true, sparse_y_pred=sparse_y_pred, axis=axis)

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.math.argmax(y_pred, axis=-1)
        return super().update_state(y_true, y_pred, sample_weight)