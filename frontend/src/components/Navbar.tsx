export default function Navbar() {
  return (
    <nav
      className="
      fixed
      top-6
      left-1/2
      -translate-x-1/2
      z-50
      w-[94%]
      max-w-7xl
      rounded-full
      border
      border-zinc-800
      bg-black/70
      backdrop-blur-xl
      px-8
      py-4
      flex
      items-center
      justify-between
    "
    >
      <div className="text-xl font-bold tracking-tight">
        LearnTube
      </div>

      <div className="hidden md:flex items-center gap-8 text-sm text-zinc-400">
        <a
          href="#"
          className="hover:text-white transition"
        >
          Home
        </a>

        <a
          href="#"
          className="hover:text-white transition"
        >
          Features
        </a>

        <a
          href="#"
          className="hover:text-white transition"
        >
          History
        </a>
      </div>

      <button
        className="
        rounded-full
        bg-white
        text-black
        px-5
        py-2
        font-semibold
        hover:bg-zinc-200
        transition
      "
      >
        GitHub
      </button>
    </nav>
  );
}
