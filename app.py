terraform {
  backend "s3" {
    bucket = "nareshitdevopstest"
    key = "
    #use_lockfile = "true" #s3 supports this feature but terraform latest version >1.10
    dynamodb_table = "axajxas"
    encrypt = true
  }
}
