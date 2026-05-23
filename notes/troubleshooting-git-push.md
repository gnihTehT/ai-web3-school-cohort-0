# Git Push 踩坑记录

## 问题
本地 commit 后 `git push origin main` 失败，提示:
```
! [rejected]        main -> main (fetch first)
remote contains work that you do not have locally
```

## 原因
仓库在别的设备上也被 push 过，产生了分叉历史。

## 解决步骤
1. `git fetch origin` — 获取最新远程状态
2. `git rebase origin/main` — 将本地 commit 重放到远程最新 commit 之上
3. `git push origin main` — 正常推送

如果 rebase 后仍失败（提示 "Everything up-to-date" 但文件没上远程），备用方案：
- 直接用 GitHub API 创建文件: `gh api --method PUT /repos/.../contents/... -f content="$base64_content"`

## 教训
- 在多个设备上操作同一个分支时，push 前先 `git pull --rebase`
- 用 API 创文件绕过 git push 时，注意本地和远程会不同步
