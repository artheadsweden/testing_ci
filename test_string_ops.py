import string_ops


class TestStringOps:
    def test_remove_vowels(self):
        assert string_ops.remove_vowels("Joakim") == "Jkm"

    def test_reverse_string(self):
        assert string_ops.reverse_string("Joakim") == "mikaoJ"

    def test_translate_to_robber(self):
        assert string_ops.translate_to_robber("thIs is fun") == "tothohisos isos fofunon"
