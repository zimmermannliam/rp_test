from submodules.radiance_pipeline.radiance_data import RadianceData
from submodules.radiance_pipeline.radiance_pipeline import radiance_pipeline
import sys

def test1():
    rd = RadianceData(
            diameter = 3612,
            crop_x_left = 1019,
            crop_y_down = 74,
            view_angle_vertical = 186,
            view_angle_horizontal = 186,
            target_x_resolution = 1000,
            target_y_resolution = 1000,
            paths_ldr = ["/home/lpz/Downloads/selected_images/Selected_Images/*.JPG"],
            path_temp = "/home/lpz/school/rp_test/submodules/Intermediate/",
            path_rsp_fn = "/home/lpz/school/rp_test/submodules/radiance_pipeline/Inputs/Parameters/Response_function.rsp",
            path_vignetting = "/home/lpz/school/rp_test/submodules/radiance_pipeline/Inputs/Parameters/vignetting_f5d6.cal",
            path_fisheye = "/home/lpz/school/rp_test/submodules/radiance_pipeline/Inputs/Parameters/fisheye_corr.cal",
            path_ndfilter = "/home/lpz/school/rp_test/submodules/radiance_pipeline/Inputs/Parameters/NDfilter_no_transform.cal",
            path_calfact = "/home/lpz/school/rp_test/submodules/radiance_pipeline/Inputs/Parameters/CF_f5d6.cal",
            path_errors = "",
            path_logs = ""
            )

    radiance_pipeline(rd)

def test2():
    rd = RadianceData(
            diameter = 3612,
            crop_x_left = 1019,
            crop_y_down = 74,
            view_angle_vertical = 186,
            view_angle_horizontal = 186,
            target_x_resolution = 1000,
            target_y_resolution = 1000,
            paths_ldr = ["/home/lpz/Downloads/selected_images/Selected_Images/*.JPG"],
            path_temp = "/home/lpz/school/rp_test/submodules/Intermediate/",
            path_rsp_fn = None,
            path_vignetting = None,
            path_fisheye = None,
            path_ndfilter = None,
            path_calfact = None,
            path_errors = "",
            path_logs = ""
            )

    radiance_pipeline(rd)
    

def main():
    tests = [test1, test2]
    for arg in sys.argv[1:]:
        tests[int(arg)]()


if __name__ == "__main__":
    main()
