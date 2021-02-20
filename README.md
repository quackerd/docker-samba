# docker-samba

[![Build Status](https://ci.quacker.org/api/badges/d/docker-samba/status.svg)](https://ci.quacker.org/d/docker-samba)

## What is this?
This is Samba server in Docker. The image is designed for flexbility and maintainability. You are expected to supply your own smb.conf and user/group configs. You also need to maintain the proper permissions for shared folders, which usually only need to be done correctly once at the beginning.

TL;DR: if you are familiar with Samba configuration, this image is for you.

## Usage
### Volumes
- `/samba/smb.conf`: the Samba configuration file that the container uses.
- `/samba/[share]`: please map your Samba share folders to `/samba/` in the container.

### Environment Variables
- `GROUPS`: group configurations. Format: `[group name],[group id]`. Connect multiple group configs with `;`.
- `USERS`: user configurations. Format: `[username],[user id],[samba password],[additional group names*]`. `*`: this option is optional and you can specify multiple groups using `,` as separator.  
- `SMBD_ARGS`: additional parameters for `smbd`. E.g. `-d 2` which enables debug output.

### docker-compose
Please see the `example` folder. 

## Updating
`docker-compose pull && docker-compose down && docker-compose up -d`

## Troubleshooting
It's always helpful to add `-d 2` to `SMBD_ARGS` for samba debug output.

### Q: I can't access mounted config file or directories?
Are you running SELinux? If so you need to set the correct tag on mounted volumes `chcon -t svirt_sandbox_file_t [your file/folder]`
