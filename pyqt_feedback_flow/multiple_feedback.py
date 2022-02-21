from PyQt5.QtCore import QEasingCurve, QPoint
from PyQt5.QtWidgets import QApplication

from pyqt_feedback_flow.feedback import (AnimationDirection, AnimationType,
                                         ImageFeedback)


class MultipleImageFeedback(object):
    """
    Class for giving multiple image feedback
    in the form of toast notifications.\n
    Args:
        number_of_images (int): desired number of notifications
        img (str): path to the image
        width (int): width of the image
        height (int): height of the image
    """
    def __init__(self,
                 number_of_images: int,
                 img: str,
                 width: int = 100,
                 height: int = 100) -> None:
        """
        Initialisation method for MultipleImageFeedback class.\n
        Args:
            number_of_images (int): desired number of notifications
            img (str): path to the image
            width (int): width of the image
            height (int): height of the image
        """
        self.number_of_images = number_of_images
        self.img = img
        self.notification_width = width
        self.notification_height = height
        self.notifications = (number_of_images *
                              [ImageFeedback(img, width, height)])

    def show(self,
             type_of_animation: int,
             animation_direction: int,
             time: int = 3000,
             curve: int = QEasingCurve.OutInQuart) -> None:
        """
        Method for displaying a toast notification.\n
        Args:
            type_of_animation (int): one of the preset types of animations
                                     in AnimationType enum class
            animation_direction (int): one of the preset directions of
                                       animations in AnimationDirection
                                       enum class
            time (int): desired time of the flow in milliseconds
            curve (int): the type of easing curve of the animation
        """
        # Obtaining the screen size.
        screen = QApplication.primaryScreen().size()
        width = screen.width()
        height = screen.height()

        points = []
        for i in range(self.number_of_images):
            # Vertical animation.
            if type_of_animation == AnimationType.VERTICAL:
                if animation_direction == AnimationDirection.UP:
                    start = QPoint(100 * i, height - self.notification_height)
                    end = QPoint(100 * i, 0)
                elif animation_direction == AnimationDirection.DOWN:
                    start = QPoint(i, 0)
                    end = QPoint(i, height - self.notification_height)
                else:
                    raise Exception("""Incorrect combination of animation
                                       type and direction.""")
            # Horizontal animation.
            elif type_of_animation == AnimationType.HORIZONTAL:
                if animation_direction == AnimationDirection.LEFT:
                    start = QPoint(width - self.notification_width,
                                   height // 2 - self.notification_height // 2)
                    end = QPoint(0,
                                 height // 2 - self.notification_height // 2)
                elif animation_direction == AnimationDirection.RIGHT:
                    start = QPoint(0,
                                   height // 2 - self.notification_height // 2)
                    end = QPoint(width - self.notification_width,
                                 height // 2 - self.notification_height // 2)
                else:
                    raise Exception("""Incorrect combination of animation
                                       type and direction.""")
            # Main diagonal animation.
            elif type_of_animation == AnimationType.MAIN_DIAGONAL:
                if animation_direction == AnimationDirection.LEFT or \
                   animation_direction == AnimationDirection.UP:
                    start = QPoint(width - self.notification_width,
                                   height - self.notification_height)
                    end = QPoint(0, 0)
                elif (animation_direction == AnimationDirection.RIGHT or
                      animation_direction == AnimationDirection.DOWN):
                    start = QPoint(0, 0)
                    end = QPoint(width - self.notification_width,
                                 height - self.notification_height)
                else:
                    raise Exception("""Incorrect combination of animation
                                       type and direction.""")
            # Antidiagonal animation.
            elif type_of_animation == AnimationType.ANTI_DIAGONAL:
                if animation_direction == AnimationDirection.RIGHT or \
                   animation_direction == AnimationDirection.UP:
                    start = QPoint(0, height - self.notification_height)
                    end = QPoint(width - self.notification_width, 0)
                elif (animation_direction == AnimationDirection.LEFT or
                      animation_direction == AnimationDirection.DOWN):
                    start = QPoint(width - self.notification_width, 0)
                    end = QPoint(0, height - self.notification_height)
                else:
                    raise Exception("""Incorrect combination of animation
                                       type and direction.""")

            points.append((start, end))

        p0, p1 = points[0]
        self.notifications[0].flow(p0, p1, time, curve)
        p0, p1 = points[4]
        self.notifications[4].flow(p0, p1, time, curve)
