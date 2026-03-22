# Ayuda Memoria — Rodo's Dev Notes
## Week 1 — Terminal Commands

### Navigation
pwd              → where am I?
ls               → what's in here?
ls -la           → detailed list (type, size, permissions)
cd foldername    → move into a folder
cd ..            → go up one level
cd ~             → go to home folder

### Files & Folders
mkdir foldername       → create a new folder
touch filename.py      → create a new empty file
cat filename.py        → print file contents in terminal
mv file.py ~/projects/ → move a file
mv *.py ~/projects/    → move ALL .py files at once
mv old.py new.py       → rename a file
rm -r foldername       → delete folder and everything inside
code .                 → open VS Code here
code filename.py       → open specific file in VS Code

### Running Python
python3 filename.py    → run a Python file
python3 --version      → check Python version

## Week 2 — Git & GitHub

### Daily Workflow (use these every day!)
git status             → what changed? what's staged?
git add .              → stage ALL changed files
git add filename.py    → stage one specific file
git commit -m "msg"    → take a snapshot
git push               → upload to GitHub
git log --oneline      → see commit history
git diff abc def       → see what changed between commits

### Setup (run once per project)
git init               → start tracking a folder
git branch -m main     → name the branch main
git remote add origin URL → connect to GitHub
git push -u origin main   → first push ever

### Branches
git checkout -b name   → create branch and switch to it
git checkout main      → switch back to main
git branch             → list all branches (* = current)
git merge branchname   → merge branch into current
git branch -d name     → delete branch after merging

### Daily rhythm
1. make changes
2. git add .
3. git commit -m "what I did"
4. git push