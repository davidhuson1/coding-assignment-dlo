from dlo import generateToken


def test_generate_token_default():
    message = "nonce4615bccd-82a2-4143-b3c4-69e5e6e55cc8timestamp2024-10-06T20:20:25.225072+02:00userid1usertypeclient"
    secret = "q1wZ91XT5y/qS+WzE7vrR//Oxt94honcMYG2G4ylCCJuTV1ZjSzPo7jCUug="
    token = generateToken(message, secret)

    assert (
        token
        == "9acae4f9633aaf9a4a12fa5d7a40b97826d5c7a0743e3ecffee94877b50996125043315bd6445fd98aa905663505fb8ea9915d555c04ef1976993d148650e92a"
    )
