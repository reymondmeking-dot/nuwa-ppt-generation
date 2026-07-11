# Changelog

## 1.0.1 - 2026-07-11

- Fixed `nuwa-ppt build` parsing so documented options after the project path work.
- Stopped loading an arbitrary current-directory `.env` unless explicitly opted in.
- Added TLS verification, redirect revalidation, SSRF protection, and response-size limits to web/document imports.
- Confined HTML `file://` and relative image imports to the source document directory.
- Added bounded ZIP/OOXML handling for PPTX, DOCX, EPUB, and XLSX inputs: at most 10,000 members, 256 MiB per member, and 1 GiB total expanded data.
- Rejected archive path traversal, duplicate/encrypted members, and symbolic links before reads or extraction.
- Added loopback Host/Origin validation and random HttpOnly write-session protection to the local confirmation and SVG editor UIs.
- Included Flask in the documented `full` optional dependency set used by the local UIs.
- Cleared the full legacy script lint baseline, including an undefined `argparse` annotation and unused/dead code.
- Added regression tests and CI test execution.
