# Errata and Improvements

## Page 173, Chapter 5
The book stated the Nokia SR Linux default username and password are both admin. This is true prior to release 22.11.1. 
The username for releases after that version is still admin, but the password is set to NokiaSr1!, please see https://containerlab.dev/manual/kinds/srl/.

## CML NX-OSv no longer available in the latest CML
Thank you [Grana2codes](https://github.com/Grana2codes), Paolo G., Jilles C. for pointing out the issue. In the latest CML, NX-OSv is still available for use within CML, but no longer included in teh refplat IOS image (more information [here](https://developer.cisco.com/docs/modeling-labs/#!nx-os/overview)). You can still download the image [here](https://developer.cisco.com/docs/modeling-labs/#!downloading-files-for-cml-installation). Or you can update the image definition from nxosv to nxosv9000 instead. 
