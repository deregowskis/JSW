import tensorflow as tf
# CNN
def recognize(img):
    """
    :param img: 输入图像矩阵
    :return: 模型所预测的字符
    """
    img = img.resize((28, 28), Image.ANTIALIAS)  # 转换为模型对应的输入尺寸(28, 28)
    # img.show()                                 # 可视化待识别图像
    myimage = np.array(img.convert('L'))         # 灰度化
    img_arr = myimage / 255.0                    # 归一化，转换为模型对应的输入值区间0-1

    # 构建模型结构
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), padding='same'),  # 2d卷积，输出通道16
        tf.keras.layers.BatchNormalization(),                                    # BN,防止过拟合
        tf.keras.layers.Activation('relu'),                                      # relu激活函数
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='same'),  # 池化，降低维度
        tf.keras.layers.Dropout(0.2),                                            # Dropout 随机舍弃

        tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding='same'),  # 2d卷积，输出通道32
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2, padding='same'),
        tf.keras.layers.Dropout(0.2),

        tf.keras.layers.Flatten(),                                                # 拉直，送入全连接层
        tf.keras.layers.Dense(128, activation='relu'),                            # 全连接层，128个隐藏节点
        tf.keras.layers.Dropout(0.2),                                             # Dropout 随机舍弃,防止过拟合
        tf.keras.layers.Dense(10, activation='softmax')                           # softmax输出最终预测的10个值概率向量
    ])

    model_save_path = './model/mnist.ckpt'     # 训练好的模型保存的路径
    model.load_weights(model_save_path)        # 加载模型权重

    x_predict = img_arr.reshape(1, 1, 28, 28)  # 将输入格式化，使之对应网络输入(batch_size, input_chanel, wsize, dsize)
    result = model.predict(x_predict)          # 预测

    pred = tf.argmax(result, axis=1)           # 输出为向量形式，取概率最大的下标为pred
    # print("pred", pred.numpy())

    return pred.numpy()[0]                     # 返回单个字符