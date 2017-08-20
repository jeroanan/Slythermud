class State1(object):

    __sInfo = None
    __config = None

    def __init__(self, sInfo, config):
        self.__sInfo = sInfo
        self.__config = config

    def enter(self):
        banner_filename = "{}/banner".format(self.__config.text_dir)
        banner = ''

        with open(banner_filename) as bf:
            banner = bf.read()

        for i, bLines in enumerate(banner.split('\n')):
            if i < len(bLines) - 1:
                self.__sInfo.sendString(bLines)
            else:
                self.__sInfo.sendString(bLines, 0)			

    def process_input(self, data):
        pass
