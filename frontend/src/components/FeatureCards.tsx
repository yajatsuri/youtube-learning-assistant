const features = [
  {
    title: "Executive Summary",
    description:
      "Quickly understand the core ideas of any YouTube video.",
  },
  {
    title: "Detailed Notes",
    description:
      "AI-generated structured notes for revision and learning.",
  },
  {
    title: "Key Takeaways",
    description:
      "Extract the most important actionable insights instantly.",
  },
];

export default function FeatureCards() {
  return (
    <section className="max-w-6xl mx-auto px-6 py-24">

      <div className="grid md:grid-cols-3 gap-8">

        {features.map((feature) => (
          <div
            key={feature.title}
            className="
            rounded-3xl
            border
            border-zinc-800
            bg-zinc-900/40
            p-8
            transition-all
            duration-300
            hover:border-zinc-600
            hover:-translate-y-1
          "
          >
            <h3 className="text-2xl font-bold mb-4">
              {feature.title}
            </h3>

            <p className="text-zinc-400 leading-7">
              {feature.description}
            </p>
          </div>
        ))}

      </div>

    </section>
  );
}

