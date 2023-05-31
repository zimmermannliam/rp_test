import sys
import os

from submodules.radiance_pipeline.radiance_data import RadianceData
from submodules.radiance_pipeline.radiance_pipeline import radiance_pipeline

def test0():
    rd = RadianceData(
            diameter = 3612,
            crop_x_left = 1019,
            crop_y_down = 74,
            view_angle_vertical = 186,
            view_angle_horizontal = 186,
            target_x_resolution = 1000,
            target_y_resolution = 1000,
            paths_ldr = ["/home/lpz/work/rp_test/example_desk/input_images/*.JPG"],
            path_temp = "/home/lpz/work/rp_test/temp/",
            path_rsp_fn = "/home/lpz/work/rp_test/example_desk/Response_function.rsp",
            path_vignetting = "/home/lpz/work/rp_test/example_desk/vignetting_f5d6.cal",
            path_fisheye = "/home/lpz/work/rp_test/example_desk/fisheye_corr.cal",
            path_ndfilter = "/home/lpz/work/rp_test/example_desk/NDfilter_no_transform.cal",
            path_calfact = "/home/lpz/work/rp_test/example_desk/CF_f5d6.cal"
            )

    radiance_pipeline(rd)


def test1():
    rd = RadianceData(
            diameter = 3612,
            crop_x_left = 1019,
            crop_y_down = 74,
            view_angle_vertical = 186,
            view_angle_horizontal = 186,
            target_x_resolution = 1000,
            target_y_resolution = 1000,
            paths_ldr = ["/home/lpz/work/rp_test/example_desk/input_images/*.JPG"],
            path_temp = "/home/lpz/work/rp_test/temp/",
            path_rsp_fn = None,
            path_vignetting = None,
            path_fisheye = None,
            path_ndfilter = None,
            path_calfact = None
            )

    radiance_pipeline(rd)


def test2():
    rd = RadianceData(
            diameter = 1100,
            crop_x_left = 259,
            crop_y_down = 34,
            view_angle_vertical = 180,
            view_angle_horizontal = 180,
            target_x_resolution = 1000,
            target_y_resolution = 1000,
            paths_ldr = ["/home/lpz/work/rp_test/example_belal/2.LDRImages/IMG_6*.JPG"],
            path_temp = "/home/lpz/work/rp_test/temp/",
            path_rsp_fn = "/home/lpz/work/rp_test/example_belal/3.Parameters/Response_function.rsp",
            path_vignetting = "/home/lpz/work/rp_test/example_belal/3.Parameters/vignetting.cal",
            path_fisheye = None,
            path_ndfilter = None,
            path_calfact = "/home/lpz/work/rp_test/example_belal/3.Parameters/CF.cal"
            )

    radiance_pipeline(rd)


def test3():
    rd = RadianceData(
            diameter = 1100,
            crop_x_left = 259,
            crop_y_down = 34,
            view_angle_vertical = 180,
            view_angle_horizontal = 180,
            target_x_resolution = 1000,
            target_y_resolution = 1000,
            paths_ldr = ["/home/lpz/work/rp_test/example_belal/2.LDRImages/IMG_7*.JPG"],
            path_temp = "/home/lpz/work/rp_test/temp/",
            path_rsp_fn = "/home/lpz/work/rp_test/example_belal/3.Parameters/Response_function.rsp",
            path_vignetting = "/home/lpz/work/rp_test/example_belal/3.Parameters/vignetting.cal",
            path_fisheye = None,
            path_ndfilter = None,
            path_calfact = "/home/lpz/work/rp_test/example_belal/3.Parameters/CF.cal"
            )

    radiance_pipeline(rd)

def main():
    tests = [test0, test1, test2, test3]
    stats = {}
    for arg in sys.argv[1:]:
        tests[int(arg)]()
        stats[int(arg)] = os.stat("/home/lpz/work/rp_test/temp/output10.hdr")
    for key,val in stats.items():
        print(f"{key}: {val}\n")


if __name__ == "__main__":
    main()
