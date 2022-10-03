class VersionInfoFactory:
    def createVersion(hash_value, size_value):
        # [
        #     {
        #         hash: 버전별 hasded name,
        #         size: file 사이즈
        #     },
        #     ...
        # ]
        version_info = {
            "hash"      : hash_value,
            "size"      : size_value
        }

        return version_info