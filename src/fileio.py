import color_convert
from imagemat import ImageMat

# 画像読み込み関数
def read_image(filename):
    image_mat = ImageMat()
    
    with open(filename, 'rb') as image_file: #バイナリデータとして画像を読み込む
        # ファイルサイズを取得
        image_file.seek(0, 2)  # ファイルの終わりへ
        size = image_file.tell()  # 現在のファイルポインタ位置 = ファイルサイズ
        print(f"file_size: {size}")
        
        # ファイルの最初に戻る
        image_file.seek(0)
        
        # ヘッダーを読み込み
        image_mat.m_header = list(image_file.read(54))
        
        # 画像サイズとピクセルデータの情報を抽出
        image_mat.m_width = image_mat.m_header['数字'] + \
                            image_mat.m_header['数字'] * 256 + \
                            image_mat.m_header['数字'] * 256**2 + \
                            image_mat.m_header['数字'] * 256**3
        
        image_mat.m_height = image_mat.m_header['数字'] + \
                             image_mat.m_header['数字'] * 256 + \
                             image_mat.m_header['数字'] * 256**2 + \
                             image_mat.m_header['数字'] * 256**3
        
        image_mat.m_length = image_mat.m_header['数字'] + \
                             image_mat.m_header['数字'] * 256 + \
                             image_mat.m_header['数字'] * 256**2 + \
                             image_mat.m_header['数字'] * 256**3
        
        # ピクセルデータを読み込み
        image_mat.m_pixels = list(image_file.read(image_mat.m_length))
        
        print(f"loaded image: {image_mat.m_width} x {image_mat.m_height}")
    
    return image_mat

# 画像書き込み関数
def write_image(image, filename):
    if image.m_ch == 1:
        pseudo_gray = color_convert.gray2color(image)
        write_image(pseudo_gray, filename)
        return
    
    with open(filename, 'wb') as image_file:
        # 縦, 横の大きさを再度求める
        # 処理によって画像サイズが変化した場合に必要
        image_header = image.m_header.copy()
        
        #ヘッダーにファイルサイズの情報を格納する処理
        #参考にして下のfor文に処理を記述してみてください
        a = image.m_length + 54
        for i in range(2, 6):
            image_header[i] = a % 256
            a /= 256

        width = image.m_width
        for i in range('数字', '数字'):
            #処理を記述
            continue #処理記述後削除
        
        height = image.m_height
        for i in range('数字', '数字'):
            #処理を記述
            continue #処理記述後削除
        
        image_header['数字'] = image.m_ch
        
        length = image.m_length
        for i in range('数字', '数字'):
            #処理を記述
            continue #処理記述後削除
        
        # ヘッダーとピクセルデータを書き込み
        image_file.write(bytearray(image_header))
        image_file.write(bytearray(image.m_pixels))
        
        print(f"wrote image: {image.m_width} x {image.m_height}")


# # 使用例
# if __name__ == "__main__":
#     img = read_image("img/cube.bmp")
#     write_image(img, "output_image.bmp")
