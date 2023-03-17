# 开发时间：2023/3/17 21:48


class IframeBaiduMapBase:
    def search_button(self):
        '''
        定位百度地图搜索按钮
        :return:
        '''
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"

