(+ 2 3)

(map (fn [n] (+ n (* n 10))) (range 1 10))

(defn minimum-height
  [base area]
  (int (Math/ceil (/ (* 2 area) base))))

(minimum-height 3 8)

(defn factorial [n]
  (reduce * (range 1 (inc n))))

(factorial 10)

(defn fib
  [k]
  (case k
    1 0
    2 1
    3 1
    (+ (fib (- k 1)) (fib (- k 2)))))

(fib 13)
