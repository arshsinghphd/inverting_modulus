from pdf2image import convert_from_path
with open("pdfs.txt") as f:
    for file in f:
        file = file.strip()
        out = file[:-4]
        pages = convert_from_path(file, dpi=300)
        i = 0
        for page in pages:
            page.save(f"{out}{i}.jpg", 'JPEG')
            i += 1
'''
BWT Tutorial: Decoding_using_preset_string.pdf
BWT Tutorial: Decoding_using_user_provided_string.pdf
BWT Tutorial: Encoding_error1.pdf
BWT Tutorial: Encoding_error2.pdf
BWT Tutorial: Encoding_error3.pdf
BWT Tutorial: Encoding_using_preset_string.pdf
BWT Tutorial: Encoding_using_user_provided_string.pdf
BWT Tutorial: Introduction.pdf
BWT Tutorial: Optimizing Decoding_using_preset_string.pdf
BWT Tutorial: Optimizing Decoding_using_user_provided_string.pdf
'''
