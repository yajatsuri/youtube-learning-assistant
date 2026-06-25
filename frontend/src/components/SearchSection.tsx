interface SearchSectionProps {
  youtubeUrl: string;
  setYoutubeUrl: (value: string) => void;
  generateNotes: () => void;
  loading: boolean;
}

export default function SearchSection({
  youtubeUrl,
  setYoutubeUrl,
  generateNotes,
  loading,
}: SearchSectionProps) {
  return (
    <section className="max-w-5xl mx-auto px-6 -mt-8">

      <div
        className="
        rounded-[32px]
        border
        border-zinc-800
        bg-zinc-900/50
        backdrop-blur-2xl
        p-8
        shadow-2xl
      "
      >

        <div className="space-y-6">

          <input
            type="text"
            value={youtubeUrl}
            onChange={(e) => setYoutubeUrl(e.target.value)}
            placeholder="Paste a YouTube URL..."
            className="
            w-full
            rounded-2xl
            bg-black/60
            border
            border-zinc-800
            px-6
            py-5
            text-lg
            text-white
            placeholder:text-zinc-500
            outline-none
            focus:border-white
            transition
          "
          />

          <button
            onClick={generateNotes}
            disabled={loading}
            className="
            w-full
            rounded-2xl
            bg-white
            text-black
            py-5
            text-lg
            font-semibold
            hover:scale-[1.01]
            hover:bg-zinc-200
            transition-all
            duration-300
            disabled:opacity-50
          "
          >
            {loading ? "Generating..." : "Generate Notes"}
          </button>

        </div>

      </div>

    </section>
  );
}
