import re
import pytest

def delete_repository_manifest(self, registry_name, repository_name, digest):
    return self._client.request(
        "DELETE",
        f"/v2/registry/{registry_name}/repositories/{repository_name}/digests/{digest}"
    )

def delete_repository_manifest(self, registry_name, repository_name, digest):
    pattern = r"^sha256:[0-9a-f]{64}$"
    if not re.match(pattern, digest):
        raise ValueError("Invalid checksum digest format. It must be 'sha256:<64_hex_characters>'.")
    return self._client.request(
        "DELETE",
        f"/v2/registry/{registry_name}/repositories/{repository_name}/digests/{digest}"
    )


def test_delete_repository_manifest_invalid_digest(mock_client):
    with pytest.raises(ValueError):
        mock_client.registry.delete_repository_manifest("my-registry", "repo", "abcd123")
