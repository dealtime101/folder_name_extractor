# Patch notes

## 0.1.7 - 2026-10-22
- Fix FOL517.8: folder names are written in alphabetical order, ignoring case.

## 0.1.6 - 2026-10-22
- Fix FOL517.4: the output file is written as UTF-8, so folder names with non-Latin characters or emoji no longer fail on Windows.

## 0.1.5 - 2026-10-22
- Fix FOL517.6: if the output file already exists, the tool asks before replacing it. Any answer other than Y leaves the existing file untouched.

## 0.1.4 - 2026-10-22
- Fix FOL517.5: an unreadable folder or an unwritable output location now shows a clear message instead of a raw traceback.

## 0.1.3 - 2026-10-22
- Fix FOL517.2: answering Y now really opens the output file with the system's default application (Windows, macOS, Linux). If it can't be opened, a clear message is shown.

## 0.1.2 - 2026-10-22
- Fix FOL517.1: the "open the file?" prompt now honors the answer. Answering N (or anything other than Y/y) no longer prints the opening message.

## 0.1.1 - 2026-10-22
- Fix FOL517.3: the output folder no longer depends on the Windows-only USERPROFILE variable. It is now the user's home Downloads folder on any OS, and it is created if missing.

## 0.1.0
- Initial version (untagged baseline).
