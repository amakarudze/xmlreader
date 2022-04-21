from xmlreader.forms import UploadFileForm


def test_upload_file_form_valid(upload_form_valid, file_data):
    data = upload_form_valid
    form = UploadFileForm(data, file_data)
    assert form.is_multipart()
    assert form.is_valid()
    assert form.errors == {}


def test_upload_file_form_invalid(upload_form_invalid):
    form = UploadFileForm(data=upload_form_invalid)
    assert not form.is_valid()
    assert form.errors == {"file": ["This field is required."]}
