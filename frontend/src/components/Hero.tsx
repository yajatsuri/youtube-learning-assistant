export default function Hero() {
  return (
    <section
      className="
      max-w-6xl
      mx-auto
      pt-52
      pb-28
      px-6
      text-center
    "
    >
      <div
        className="
        inline-flex
        items-center
        rounded-full
        border
        border-zinc-800
        bg-zinc-900/70
        px-5
        py-2
        text-sm
        text-zinc-400
        mb-10
      "
      >
        ✦ AI Powered Learning Assistant
      </div>

      <h1
        className="
        text-6xl
        md:text-8xl
        font-black
        tracking-[-0.06em]
        leading-[0.9]
      "
      >
        Understand

        <span
          className="
          block
          bg-gradient-to-b
          from-white
          via-zinc-300
          to-zinc-700
          bg-clip-text
          text-transparent
        "
        >
          Faster.
        </span>
      </h1>

      <p
        className="
        mt-10
        max-w-3xl
        mx-auto
        text-xl
        leading-9
        text-zinc-500
      "
      >
        Turn long YouTube videos into concise summaries,
        structured notes and interview-ready takeaways
        powered by AI.
      </p>
    </section>
  );
}
