import shutil
from pathlib import Path


def main() -> None:
    input_contest_name = input("コンテスト名を入力:（例: abc000）")
    new_contest_dir_path = Path(__file__).parent / f"{input_contest_name}"
    new_contest_dir_path.mkdir(exist_ok=False)
    template_file_path = Path(__file__).parent / "atcoder_template.py"

    for problem_chr in [chr(num) for num in range(ord("A"), ord("G") + 1)]:
        problem_dir_path = new_contest_dir_path / problem_chr
        problem_dir_path.mkdir(exist_ok=False)

        shutil.copyfile(template_file_path, problem_dir_path / "main.py")
        shutil.copyfile(template_file_path, problem_dir_path / "test.py")

        print(f"created problem_{problem_chr} directory")

    return


if __name__ == "__main__":
    main()
