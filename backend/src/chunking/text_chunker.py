from pathlib import Path


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
):
    """
    Split text into overlapping chunks.

    Example:
    Chunk 1: 0-1000
    Chunk 2: 800-1800
    Chunk 3: 1600-2600
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


def main():

    input_file = Path("backend/data/extracted_text.txt")

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = chunk_text(
        text=text,
        chunk_size=1000,
        overlap=200
    )

    print(f"\nTotal Chunks: {len(chunks)}")

    print("\n" + "=" * 80)
    print("FIRST CHUNK")
    print("=" * 80)

    print(chunks[0])

    print("\n" + "=" * 80)
    print("SECOND CHUNK")
    print("=" * 80)

    print(chunks[1])

    print("\n" + "=" * 80)
    print("CHUNK STATISTICS")
    print("=" * 80)

    print(f"Document Length : {len(text):,} characters")
    print(f"Chunk Size      : 1000 characters")
    print(f"Overlap         : 200 characters")
    print(f"Total Chunks    : {len(chunks)}")


if __name__ == "__main__":
    main()