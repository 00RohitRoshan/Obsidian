- Early variable evaluation
- Provider mocking in `tofu test`
-  resource overrides `tofu test`
```yml
Since Terraform doesn't support these new language features, OpenTofu now supports the .tofu file extension. When a file with the .tofu extension is present, OpenTofu will ignore the identically named .tf file. Using this new file extension, module authors can use the new features of OpenTofu and still keep older code around for compatibility.
```