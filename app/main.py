def main():
    print("==== 文献検索システム ====")
    print("終了する場合は 'exit' と入力してください\n")

    while True:
        # ユーザーからクエリを受け取る
        query = input("検索クエリを入力してください: ").strip()

        if query.lower() == "exit":
            print("文献検索システムを終了します。")
            break

        if not query:
            print("⚠ クエリが空です。入力してください。")
            continue

        # ここで検索処理を行う（後で実装）
        results = search_documents(query)

        # 結果を表示
        print("\n=== 検索結果 ===")
        if results:
            for i, res in enumerate(results, 1):
                print(f"{i}. {res}")
        else:
            print("該当する文献は見つかりませんでした。")
        print("================\n")


def search_documents(query: str):
    """
    文献検索ロジックを実装する関数。
    現在はダミーデータを返す。
    """
    dummy_db = [
        "深層学習による自然言語処理の研究",
        "機械学習の応用と課題",
        "AI倫理と社会的影響",
        "文献検索システムの設計と実装"
    ]

    # 単純な部分一致検索（仮実装）
    return [doc for doc in dummy_db if query in doc]


if __name__ == "__main__":
    main()
