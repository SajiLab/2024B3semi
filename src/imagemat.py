class ImageMat:
    def __init__(self):
        # 初期化
        self.m_header = [0] * 54
        self.m_width = 0
        self.m_height = 0
        self.m_length = 0
        self.m_pixels = [0]*self.m_length
        self.m_ch = 3
    
    def get_pixel(self, x, y, channel):
        # 座標のピクセル値を返す
        return self.m_pixels[(y * self.m_width + x) * self.m_ch + channel]

    def set_pixel(self, x, y, channel, value):
        # 座標のピクセル値にvalueをセットする
        self.m_pixels[(y * self.m_width + x) * self.m_ch + channel] = value
