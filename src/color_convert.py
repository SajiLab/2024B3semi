from imagemat import ImageMat
from copy import deepcopy
# 3チャンネルカラー画像を1チャンネルグレースケール画像に変換
def color2gray(color_img):
    gray_img = ImageMat()
    gray_img = deepcopy(color_img)
    
    gray_img.m_ch = 1
    gray_img.m_length = gray_img.m_width * gray_img.m_height * gray_img.m_ch
    
    gray_img.m_pixels = [0] * gray_img.m_length #ピクセル値を0で初期化
    
    # 色変換処理 (RGBの平均値を計算)
    for y in range(color_img.m_height):
        for x in range(color_img.m_width):
            #処理を記述
            continue #削除

    return gray_img

# 1チャンネルグレースケール画像を3チャンネルカラー画像に変換
def gray2color(gray_img):
    color_img = ImageMat()
    color_img = deepcopy(gray_img)

    color_img.m_ch = 3
    color_img.m_length = color_img.m_width * color_img.m_height * color_img.m_ch

    color_img.m_pixels = [0] * color_img.m_length

    # 色変換処理 (グレースケール値をRGBの各チャンネルに設定)
    # 処理を記述
    
    # リターンした画像は3つのチャンネルすべてが同じ値なのでグレーになります
    return color_img




#ここから先は完成しています


# 3チャンネル画像をそれぞれのチャンネルに分割
def split_channel(img):
    if img.m_ch == 1:
        return [img]

    gray_img = color2gray(img)
    ch1 = ImageMat()
    ch2 = ImageMat()
    ch3 = ImageMat()
    ch1 = deepcopy(gray_img)
    ch2 = deepcopy(gray_img)
    ch3 = deepcopy(gray_img)
    # 各チャンネルの値を抽出
    for y in range(img.m_height):
        for x in range(img.m_width):
            ch1_value = img.get_pixel(x, y, 0)
            ch2_value = img.get_pixel(x, y, 1)
            ch3_value = img.get_pixel(x, y, 2)
            ch1.set_pixel(x, y, 0, ch1_value)
            ch2.set_pixel(x, y, 0, ch2_value)
            ch3.set_pixel(x, y, 0, ch3_value)

    return [ch1, ch2, ch3]

# 1チャンネル画像を3チャンネル画像に統合
def merge_channel(ch1, ch2, ch3):
    multi_ch_img = ImageMat()
    multi_ch_img = gray2color(ch1)
    # 各チャンネルの値を統合
    for y in range(ch1.m_height):
        for x in range(ch1.m_width):
            multi_ch_img.set_pixel(x, y, 0, ch1.get_pixel(x, y, 0))
            multi_ch_img.set_pixel(x, y, 1, ch2.get_pixel(x, y, 0))
            multi_ch_img.set_pixel(x, y, 2, ch3.get_pixel(x, y, 0))

    return multi_ch_img


# double型の画像をuint8型に変換
def double2uint8t(double_data):
    uint_data = deepcopy(double_data)

    for y in range(double_data.m_height):
        for x in range(double_data.m_width):
            for ch in range(double_data.m_ch):
                value = double_data.get_pixel(x, y, ch)
                # 値を0-255の範囲に収めてuint8に変換
                uint_value = max(0, min(int(value), 255))
                uint_data.set_pixel(x, y, ch, uint_value)

    return uint_data
