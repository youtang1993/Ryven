from NIENV import *

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class ImageBlend_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(ImageBlend_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unblend1 = None
        self.img_unblend2 = None
        self.img_blend= None


    def update_event(self, input_called=-1):
        self.img_unblend1 = self.input(0)
        alpha= self.input(1)
        alpha=int(alpha)
        self.img_unblend2=self.input(2)
        beta=int(1.0-alpha)

        self.img_blend = cv2.addWeighted(self.img_unblend1,alpha,self.img_unblend2,beta,0.0)
        self.main_widget.show_image(self.img_blend)
        self.set_output_val(0, self.img_blend)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
