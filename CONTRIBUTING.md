# Contributing to OSSVN Community

Repo này chỉ giữ onboarding và hướng dẫn contribution của OSSVN.

Bạn có thể:

- Sửa typo hoặc link.
- Cải thiện `START_HERE.md`.
- Cải thiện `guides/first-pr.md`.
- Làm rõ cách bắt đầu với OSSVN.

Concept IT phải contribution trong `it-in-plain-vietnamese`.

## Cách làm

1. Chọn issue hoặc một thay đổi nhỏ, rõ ràng.
2. Chỉ sửa đúng scope.
3. Làm phần `Trước khi mở PR` bên dưới.
4. Mở Pull Request.

## Trước khi mở PR

### 1. Kiểm tra diff

```bash
git status --short
git diff --check
git diff
```

### 2. Chạy automated checks

Từ root của repository:

```bash
python scripts/validate_repo.py
python scripts/check_links.py
```

### 3. Kiểm tra thủ công

- Preview các file Markdown đã sửa.
- Mở các external link đã thêm hoặc sửa vì `check_links.py` chỉ kiểm tra internal Markdown links.
- Nếu sửa `START_HERE.md` hoặc `guides/first-pr.md`, đi theo flow từ `START_HERE.md` tới guide và xác nhận các bước/link vẫn dẫn đúng chỗ.

### 4. Kết quả mong đợi

- `git diff --check` exit code bằng `0`.
- `python scripts/validate_repo.py` in `Repository validation passed.`.
- `python scripts/check_links.py` in `Internal Markdown links passed.`.
- Markdown render đúng và onboarding flow không có link cũ hoặc link hỏng.

Policy chung được kế thừa từ repo `.github` của Organization.
