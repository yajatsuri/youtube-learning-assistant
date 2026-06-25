interface ResultsProps {
  response: any;
}

export default function Results({
  response,
}: ResultsProps) {

  if (!response) return null;

  return (

    <section className="max-w-5xl mx-auto px-6 pb-28 space-y-8">

      <div
        className="
        rounded-3xl
        border
        border-zinc-800
        bg-zinc-900/40
        backdrop-blur-xl
        p-8
      "
      >
        <h2 className="text-3xl font-bold mb-6">
          Executive Summary
        </h2>

        <p className="leading-8 text-zinc-300">
          {response.executive_summary}
        </p>

      </div>

      <div
        className="
        rounded-3xl
        border
        border-zinc-800
        bg-zinc-900/40
        backdrop-blur-xl
        p-8
      "
      >
        <h2 className="text-3xl font-bold mb-6">
          Detailed Notes
        </h2>

        <p className="leading-8 whitespace-pre-wrap text-zinc-300">
          {response.detailed_notes}
        </p>

      </div>

      <div
        className="
        rounded-3xl
        border
        border-zinc-800
        bg-zinc-900/40
        backdrop-blur-xl
        p-8
        "
      >
        <h2 className="text-3xl font-bold mb-6">
          Key Takeaways
        </h2>

        <ul className="space-y-4 list-disc pl-6 text-zinc-300">

          {response.key_takeaways?.map(
            (
              item: string,
              index: number
            ) => (
              <li key={index}>
                {item}
              </li>
            )
          )}

        </ul>

      </div>

    </section>

  );

}
