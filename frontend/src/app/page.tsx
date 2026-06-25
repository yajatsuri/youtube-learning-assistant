"use client";

import { useState } from "react";

import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import SearchSection from "@/components/SearchSection";
import FeatureCards from "@/components/FeatureCards";
import Results from "@/components/Results";

export default function Home() {

  const [youtubeUrl, setYoutubeUrl] = useState("");

  const [response, setResponse] = useState<any>(null);

  const [loading, setLoading] = useState(false);

  async function generateNotes() {

    try {

      setLoading(true);

      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/generate-notes`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            youtube_url: youtubeUrl,
          }),
        }
      );

      const text = await res.text();

      if (!res.ok) {
        throw new Error(
          `Backend Error ${res.status}: ${text}`
        );
      }

      setResponse(
        JSON.parse(text)
      );

    } catch (err) {

      alert(
        err instanceof Error
          ? err.message
          : "Something went wrong."
      );

    } finally {

      setLoading(false);

    }

  }

  return (

    <main className="min-h-screen">

      <Navbar />

      <Hero />

      <SearchSection
        youtubeUrl={youtubeUrl}
        setYoutubeUrl={setYoutubeUrl}
        generateNotes={generateNotes}
        loading={loading}
      />

      {!response && (

        <FeatureCards />

      )}

      <Results
        response={response}
      />

    </main>

  );

}
