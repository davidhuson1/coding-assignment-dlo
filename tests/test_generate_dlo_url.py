from freezegun import freeze_time
from unittest import mock
from dlo import generateDloUrl


@freeze_time("2024-01-12")
def test_generate_dlo_url_default():
    with mock.patch("uuid.uuid4", return_value="78d891c9-e3a4-40df-9055-c90b545b6f48"):
        userid = "1"
        usertype = "client"
        baseUrl = "https://ca-dadpktfmbz.minddistrict.dev/"
        pathToOpen = ""
        url = generateDloUrl(userid, usertype, baseUrl, pathToOpen)

        assert (
            url
            == "https://ca-dadpktfmbz.minddistrict.dev/?usertype=client&userid=1&nonce=78d891c9-e3a4-40df-9055-c90b545b6f48&timestamp=2024-01-12T00%3A00%3A00%2B02%3A00&token=83133435e59c10db376f2615d81fb194b298f069b482481552ed0fb6635e8580cb4c70f35ba8f83f1348d14735a07349961c88ffd01cf8825352b40e3f06cfa2"
        )


@freeze_time("2024-01-12")
def test_generate_dlo_url_path():
    with mock.patch("uuid.uuid4", return_value="78d891c9-e3a4-40df-9055-c90b545b6f48"):
        userid = "1"
        usertype = "client"
        baseUrl = "https://ca-dadpktfmbz.minddistrict.dev/"
        pathToOpen = "conversations"
        url = generateDloUrl(userid, usertype, baseUrl, pathToOpen)

        assert (
            url
            == "https://ca-dadpktfmbz.minddistrict.dev/conversations?usertype=client&userid=1&nonce=78d891c9-e3a4-40df-9055-c90b545b6f48&timestamp=2024-01-12T00%3A00%3A00%2B02%3A00&token=83133435e59c10db376f2615d81fb194b298f069b482481552ed0fb6635e8580cb4c70f35ba8f83f1348d14735a07349961c88ffd01cf8825352b40e3f06cfa2"
        )
