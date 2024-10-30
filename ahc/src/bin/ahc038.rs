use proconio::input;

/*
・操作は最大10^5回
・全部のたこ焼きを目的地に持っていくことが重要，最優先
・全ターン数をとにかく最小化したい
*/

fn make_coordinates_from_01_s_lines(s_lines_input: &[String]) -> Vec<Vec<usize>> {
    let mut res_coordinates: Vec<Vec<usize>> = vec![];
    for (i, cur_s_line) in s_lines_input.iter().enumerate() {
        for j in 0..cur_s_line.len() {
            if cur_s_line.chars().nth(j) == Some('1') {
                res_coordinates.push(vec![i, j]);
            }
        }
    }

    res_coordinates
}

fn solve1(
    coordinates_takoyaki_init: &[Vec<usize>],
    coordinates_takoyaki_objective: &[Vec<usize>],
    root_coordinate_init: &[usize],
) {
    /*
    頂点数2で，根から右に長さ一の辺が一本生えただけのロボットアーム
    愚直に動かしていく
     */
    // 根の位置を初期化

    fn print_u_or_d_by_displacement_r(displacement_r: &isize, last_chr: &str) {
        if *displacement_r < 0 {
            println!("U..{last_chr}");
        }
        if *displacement_r > 0 {
            println!("D..{last_chr}");
        }
    }

    fn print_l_or_r_by_displacement_c(displacement_c: &isize, last_chr: &str) {
        if *displacement_c < 0 {
            println!("L..{last_chr}");
        }
        if *displacement_c > 0 {
            println!("R..{last_chr}");
        }
    }
    let mut root_curr: usize = root_coordinate_init[0];
    let mut root_curc: usize = root_coordinate_init[1];

    // 出力パート1
    println!("2");
    println!("0 1");
    println!("{root_curr} {root_curc}");

    let mut not_put_takoyaki_vec: Vec<usize> = vec![];
    for i in 0..coordinates_takoyaki_init.len() {
        // たこ焼き取りに行く
        let takoyaki_init_r: usize = coordinates_takoyaki_init[i][0];
        let takoyaki_init_c: usize = coordinates_takoyaki_init[i][1];
        let takoyaki_objective_r: usize = coordinates_takoyaki_objective[i][0];
        let takoyaki_objective_c: usize = coordinates_takoyaki_objective[i][1];
        if takoyaki_init_c == 0 || takoyaki_objective_c == 0 {
            not_put_takoyaki_vec.push(i);
            continue;
        }

        let mut sum_move_cnt: usize = 0;
        let mut chr_pick: &str = ".";

        let cur_displacement1_r: isize = takoyaki_init_r as isize - root_curr as isize;
        let cur_displacement1_c: isize = takoyaki_init_c as isize - root_curc as isize - 1;
        let sum_move: usize = (cur_displacement1_r.abs() + cur_displacement1_c.abs()) as usize;

        if sum_move == 0 {
            println!("...P")
        }
        for _move_cnt_r in 0..cur_displacement1_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement1_r, chr_pick);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement1_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement1_c, chr_pick);
        }

        assert_eq!(
            root_curr as isize + cur_displacement1_r,
            takoyaki_init_r as isize
        );
        assert_eq!(
            root_curc as isize + cur_displacement1_c,
            takoyaki_init_c as isize - 1
        );
        assert_eq!(sum_move, sum_move_cnt);
        root_curr = takoyaki_init_r;
        root_curc = takoyaki_init_c - 1;

        // たこ焼き置きに行く

        let cur_displacement2_r: isize = takoyaki_objective_r as isize - root_curr as isize;
        let cur_displacement2_c: isize = takoyaki_objective_c as isize - root_curc as isize - 1;
        let sum_move: usize = (cur_displacement2_r.abs() + cur_displacement2_c.abs()) as usize;
        sum_move_cnt = 0;

        if sum_move == 0 {
            println!("...P")
        }
        chr_pick = ".";
        for _move_cnt_r in 0..cur_displacement2_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement2_r, chr_pick);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement2_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement2_c, chr_pick);
        }

        assert_eq!(
            root_curr as isize + cur_displacement2_r,
            takoyaki_objective_r as isize
        );
        assert_eq!(
            root_curc as isize + cur_displacement2_c,
            takoyaki_objective_c as isize - 1
        );
        assert_eq!(sum_move, sum_move_cnt);
        root_curr = takoyaki_objective_r;
        root_curc = takoyaki_objective_c - 1;
    }
}

fn solve2(
    coordinates_takoyaki_init: &[Vec<usize>],
    coordinates_takoyaki_objective: &[Vec<usize>],
    root_coordinate_init: &[usize],
    n: usize,
) {
    fn print_by_hand(cur_use_hand: &str, last_chr: &str, way: &str) {
        if cur_use_hand == "U" {
            println!("{way}......{last_chr}..");
        } else if cur_use_hand == "D" {
            println!("{way}........{last_chr}");
        } else if cur_use_hand == "L" {
            println!("{way}.......{last_chr}.");
        } else if cur_use_hand == "R" {
            println!("{way}.....{last_chr}...");
        } else {
            assert_eq!(1, 2)
        }
    }

    fn print_u_or_d_by_displacement_r(displacement_r: &isize, last_chr: &str, cur_use_hand: &str) {
        if *displacement_r < 0 {
            print_by_hand(cur_use_hand, last_chr, "U");
        }
        if *displacement_r > 0 {
            print_by_hand(cur_use_hand, last_chr, "D");
        }
    }

    fn print_l_or_r_by_displacement_c(displacement_c: &isize, last_chr: &str, cur_use_hand: &str) {
        if *displacement_c < 0 {
            print_by_hand(cur_use_hand, last_chr, "L");
        }
        if *displacement_c > 0 {
            print_by_hand(cur_use_hand, last_chr, "R");
        }
    }

    fn judge(cur_use_hand: &str, cur_displacement_r: &mut isize, cur_displacement_c: &mut isize) {
        if cur_use_hand == "U" {
            *cur_displacement_r += 1;
        } else if cur_use_hand == "D" {
            *cur_displacement_r -= 1;
        } else if cur_use_hand == "R" {
            *cur_displacement_c -= 1;
        } else if cur_use_hand == "L" {
            *cur_displacement_c += 1;
        } else {
            assert_eq!(1, 2)
        }
    }
    /*
    頂点数5で，根から東西南北に長さ１の手をはやす
    愚直に動かしていく
     */
    // 根の位置を初期化
    let mut root_curr: isize = root_coordinate_init[0] as isize;
    let mut root_curc: isize = root_coordinate_init[1] as isize;

    // 出力パート1, 回転もさせてしまう
    println!("5");
    println!("0 1");
    println!("0 1");
    println!("0 1");
    println!("0 1");
    println!("{root_curr} {root_curc}");
    println!("..LLR.....");
    println!("...L......");

    let mut not_put_takoyaki_vec1: Vec<usize> = vec![];
    let cur_use_hand: &str = "R";
    for i in 0..coordinates_takoyaki_init.len() {
        // たこ焼き取りに行く
        let takoyaki_init_r: usize = coordinates_takoyaki_init[i][0];
        let takoyaki_init_c: usize = coordinates_takoyaki_init[i][1];
        let takoyaki_objective_r: usize = coordinates_takoyaki_objective[i][0];
        let takoyaki_objective_c: usize = coordinates_takoyaki_objective[i][1];
        if takoyaki_init_c == 0 || takoyaki_objective_c == 0 {
            not_put_takoyaki_vec1.push(i);
            continue;
        }

        let mut sum_move_cnt: usize = 0;
        let mut chr_pick: &str = ".";

        let mut cur_displacement1_r: isize = takoyaki_init_r as isize - root_curr;
        let mut cur_displacement1_c: isize = takoyaki_init_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement1_r,
            &mut cur_displacement1_c,
        );

        let sum_move: usize = (cur_displacement1_r.abs() + cur_displacement1_c.abs()) as usize;

        if sum_move == 0 {
            not_put_takoyaki_vec1.push(i);
            continue;
        }
        for _move_cnt_r in 0..cur_displacement1_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement1_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement1_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement1_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement1_r;
        root_curc += cur_displacement1_c;

        // たこ焼き置きに行く

        let mut cur_displacement2_r: isize = takoyaki_objective_r as isize - root_curr;
        let mut cur_displacement2_c: isize = takoyaki_objective_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement2_r,
            &mut cur_displacement2_c,
        );

        let sum_move: usize = (cur_displacement2_r.abs() + cur_displacement2_c.abs()) as usize;
        sum_move_cnt = 0;

        if sum_move == 0 {
            not_put_takoyaki_vec1.push(i);
            continue;
        }
        chr_pick = ".";
        for _move_cnt_r in 0..cur_displacement2_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement2_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement2_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement2_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement2_r;
        root_curc += cur_displacement2_c;
    }

    // 上の手
    let mut not_put_takoyaki_vec2: Vec<usize> = vec![];
    let cur_use_hand: &str = "U";
    for i in 0..coordinates_takoyaki_init.len() {
        if !not_put_takoyaki_vec1.contains(&i) {
            continue;
        }
        // たこ焼き取りに行く
        let takoyaki_init_r: usize = coordinates_takoyaki_init[i][0];
        let takoyaki_init_c: usize = coordinates_takoyaki_init[i][1];
        let takoyaki_objective_r: usize = coordinates_takoyaki_objective[i][0];
        let takoyaki_objective_c: usize = coordinates_takoyaki_objective[i][1];
        if takoyaki_init_r == n - 1 || takoyaki_objective_r == n - 1 {
            not_put_takoyaki_vec2.push(i);
            continue;
        }

        let mut sum_move_cnt: usize = 0;
        let mut chr_pick: &str = ".";

        let mut cur_displacement1_r: isize = takoyaki_init_r as isize - root_curr;
        let mut cur_displacement1_c: isize = takoyaki_init_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement1_r,
            &mut cur_displacement1_c,
        );

        let sum_move: usize = (cur_displacement1_r.abs() + cur_displacement1_c.abs()) as usize;

        if sum_move == 0 {
            not_put_takoyaki_vec2.push(i);
            continue;
        }
        for _move_cnt_r in 0..cur_displacement1_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement1_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement1_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement1_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement1_r;
        root_curc += cur_displacement1_c;

        // たこ焼き置きに行く

        let mut cur_displacement2_r: isize = takoyaki_objective_r as isize - root_curr;
        let mut cur_displacement2_c: isize = takoyaki_objective_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement2_r,
            &mut cur_displacement2_c,
        );

        let sum_move: usize = (cur_displacement2_r.abs() + cur_displacement2_c.abs()) as usize;
        sum_move_cnt = 0;

        if sum_move == 0 {
            not_put_takoyaki_vec2.push(i);
            continue;
        }
        chr_pick = ".";
        for _move_cnt_r in 0..cur_displacement2_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement2_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement2_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement2_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement2_r;
        root_curc += cur_displacement2_c;
    }

    // 左の手
    let mut not_put_takoyaki_vec3: Vec<usize> = vec![];
    let cur_use_hand: &str = "L";
    for i in 0..coordinates_takoyaki_init.len() {
        if !not_put_takoyaki_vec2.contains(&i) {
            continue;
        }
        // たこ焼き取りに行く
        let takoyaki_init_r: usize = coordinates_takoyaki_init[i][0];
        let takoyaki_init_c: usize = coordinates_takoyaki_init[i][1];
        let takoyaki_objective_r: usize = coordinates_takoyaki_objective[i][0];
        let takoyaki_objective_c: usize = coordinates_takoyaki_objective[i][1];
        if takoyaki_init_c == n - 1 || takoyaki_objective_c == n - 1 {
            not_put_takoyaki_vec3.push(i);
            continue;
        }

        let mut sum_move_cnt: usize = 0;
        let mut chr_pick: &str = ".";

        let mut cur_displacement1_r: isize = takoyaki_init_r as isize - root_curr;
        let mut cur_displacement1_c: isize = takoyaki_init_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement1_r,
            &mut cur_displacement1_c,
        );

        let sum_move: usize = (cur_displacement1_r.abs() + cur_displacement1_c.abs()) as usize;

        if sum_move == 0 {
            not_put_takoyaki_vec3.push(i);
            continue;
        }
        for _move_cnt_r in 0..cur_displacement1_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement1_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement1_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement1_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement1_r;
        root_curc += cur_displacement1_c;

        // たこ焼き置きに行く

        let mut cur_displacement2_r: isize = takoyaki_objective_r as isize - root_curr;
        let mut cur_displacement2_c: isize = takoyaki_objective_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement2_r,
            &mut cur_displacement2_c,
        );

        let sum_move: usize = (cur_displacement2_r.abs() + cur_displacement2_c.abs()) as usize;
        sum_move_cnt = 0;

        if sum_move == 0 {
            not_put_takoyaki_vec3.push(i);
            continue;
        }
        chr_pick = ".";
        for _move_cnt_r in 0..cur_displacement2_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement2_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement2_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement2_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement2_r;
        root_curc += cur_displacement2_c;
    }

    // 下の手
    let cur_use_hand: &str = "D";
    for i in 0..coordinates_takoyaki_init.len() {
        if !not_put_takoyaki_vec3.contains(&i) {
            continue;
        }
        // たこ焼き取りに行く
        let takoyaki_init_r: usize = coordinates_takoyaki_init[i][0];
        let takoyaki_init_c: usize = coordinates_takoyaki_init[i][1];
        let takoyaki_objective_r: usize = coordinates_takoyaki_objective[i][0];
        let takoyaki_objective_c: usize = coordinates_takoyaki_objective[i][1];
        if takoyaki_init_r == 0 || takoyaki_objective_r == 0 {
            continue;
        }

        let mut sum_move_cnt: usize = 0;
        let mut chr_pick: &str = ".";

        let mut cur_displacement1_r: isize = takoyaki_init_r as isize - root_curr;
        let mut cur_displacement1_c: isize = takoyaki_init_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement1_r,
            &mut cur_displacement1_c,
        );

        let sum_move: usize = (cur_displacement1_r.abs() + cur_displacement1_c.abs()) as usize;

        if sum_move == 0 {
            continue;
        }
        for _move_cnt_r in 0..cur_displacement1_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement1_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement1_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement1_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement1_r;
        root_curc += cur_displacement1_c;

        // たこ焼き置きに行く

        let mut cur_displacement2_r: isize = takoyaki_objective_r as isize - root_curr;
        let mut cur_displacement2_c: isize = takoyaki_objective_c as isize - root_curc;

        judge(
            cur_use_hand,
            &mut cur_displacement2_r,
            &mut cur_displacement2_c,
        );

        let sum_move: usize = (cur_displacement2_r.abs() + cur_displacement2_c.abs()) as usize;
        sum_move_cnt = 0;

        if sum_move == 0 {
            continue;
        }
        chr_pick = ".";
        for _move_cnt_r in 0..cur_displacement2_r.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_u_or_d_by_displacement_r(&cur_displacement2_r, chr_pick, cur_use_hand);
        }
        chr_pick = ".";
        for _move_cnt_c in 0..cur_displacement2_c.abs() {
            sum_move_cnt += 1;
            if sum_move_cnt == sum_move {
                chr_pick = "P";
            }
            print_l_or_r_by_displacement_c(&cur_displacement2_c, chr_pick, cur_use_hand);
        }

        assert_eq!(sum_move, sum_move_cnt);
        root_curr += cur_displacement2_r;
        root_curc += cur_displacement2_c;
    }
}

fn remove_takoyaki_already_put_objective(
    coordinates_takoyaki_init: &mut Vec<Vec<usize>>,
    coordinates_takoyaki_objective: &mut Vec<Vec<usize>>,
) {
    let mut tmp_idx: Vec<usize> = vec![];
    for (i, cur_init_coordinate) in coordinates_takoyaki_init.iter().enumerate() {
        if let Some(remove_idx) = coordinates_takoyaki_objective
            .iter()
            .position(|x| *x == *cur_init_coordinate)
        {
            // println!("{:?}", coordinates_takoyaki_objective[remove_idx]);
            tmp_idx.push(i);
            coordinates_takoyaki_objective.remove(remove_idx);
        }
    }

    for &idx in tmp_idx.iter().rev() {
        // println!("{:?}", coordinates_takoyaki_init[idx]);
        coordinates_takoyaki_init.remove(idx);
    }

    assert_eq!(
        coordinates_takoyaki_init.len(),
        coordinates_takoyaki_objective.len()
    )
}
fn main() {
    // 入力部分
    input! {
        n: usize,
        _m: usize,
        _v: usize,
        s_lines: [String; n],
        t_lines: [String; n],
    }

    let mut coordinates_takoyaki_init = make_coordinates_from_01_s_lines(&s_lines);
    let mut coordinates_takoyaki_objective = make_coordinates_from_01_s_lines(&t_lines);
    assert_eq!(
        coordinates_takoyaki_init.len(),
        coordinates_takoyaki_objective.len()
    );

    remove_takoyaki_already_put_objective(
        &mut coordinates_takoyaki_init,
        &mut coordinates_takoyaki_objective,
    );

    // solve
    solve2(
        &coordinates_takoyaki_init,
        &coordinates_takoyaki_objective,
        &[0, 0],
        n,
    );
    //     // デバッグ出力
    //     println!("n = {}, m = {}, v = {}", n, m, v);
    //     println!("s = {coordinates_takoyaki_init:?}",);
    //     println!("t = {coordinates_takoyaki_objective:?}",);
}
