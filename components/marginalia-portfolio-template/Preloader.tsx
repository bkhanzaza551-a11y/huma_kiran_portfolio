import React, { useEffect, useState, useRef } from "react"
import gsap from "gsap"

export default function Preloader({ onComplete }: { onComplete?: () => void }) {
  const [percent, setPercent] = useState(0)
  const [hidden, setHidden] = useState(false)
  const containerRef = useRef<HTMLDivElement>(null)
  const counterObj = useRef({ val: 0 })

  useEffect(() => {
    // Prevent scrolling while preloader is active
    const originalOverflow = document.body.style.overflow
    document.body.style.overflow = "hidden"

    const ctx = gsap.context(() => {
      // Counter from 0 to 100
      gsap.to(counterObj.current, {
        val: 100,
        duration: 2.0,
        ease: "power2.out",
        onUpdate: () => {
          setPercent(Math.floor(counterObj.current.val))
        },
        onComplete: () => {
          // Curtain slide-up exit
          const tl = gsap.timeline({
            onComplete: () => {
              setHidden(true)
              document.body.style.overflow = originalOverflow
              onComplete?.()
            },
          })

          tl.to(".preloader-content", {
            y: -24,
            opacity: 0,
            duration: 0.5,
            ease: "power2.in",
          }).to(
            containerRef.current,
            {
              yPercent: -100,
              duration: 0.9,
              ease: "power4.inOut",
            },
            "-=0.15"
          )
        },
      })
    }, containerRef)

    return () => {
      ctx.revert()
      document.body.style.overflow = originalOverflow
    }
  }, [onComplete])

  if (hidden) return null

  return (
    <div
      ref={containerRef}
      className="mgn-preloader"
      style={{
        position: "fixed",
        inset: 0,
        zIndex: 999999,
        backgroundColor: "#ecebe7",
        backgroundImage: "radial-gradient(#242426 0.75px, transparent 0.75px)",
        backgroundSize: "24px 24px",
        color: "#242426",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        padding: "clamp(24px, 4vw, 56px)",
        boxSizing: "border-box",
        fontFamily: "'Poppins', sans-serif",
      }}
    >
      {/* Top Header Row matching the Portfolio cover */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          fontSize: "13px",
          letterSpacing: "0.06em",
          color: "rgba(36, 36, 38, 0.65)",
          textTransform: "uppercase",
        }}
      >
        <span>2026</span>
        <span style={{ fontWeight: 500, letterSpacing: "0.1em" }}>Curriculum Vitae</span>
        <span style={{ fontFamily: "'Caveat', cursive", fontSize: "20px", textTransform: "none", color: "#7d84ef" }}>
          portfolio
        </span>
      </div>

      {/* Center Content */}
      <div
        className="preloader-content"
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          margin: "auto 0",
        }}
      >
        {/* Monogram Badge */}
        <div
          style={{
            position: "relative",
            width: "68px",
            height: "68px",
            display: "grid",
            placeItems: "center",
            marginBottom: "16px",
          }}
        >
          <svg viewBox="0 0 100 100" style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }}>
            <circle
              cx="50"
              cy="50"
              r="44"
              fill="none"
              stroke="#7d84ef"
              strokeWidth="2.5"
              strokeDasharray="276"
              strokeDashoffset={276 - (276 * percent) / 100}
              style={{ transition: "stroke-dashoffset 0.1s linear" }}
            />
          </svg>
          <span
            style={{
              fontFamily: "'DM Serif Display', serif",
              fontSize: "26px",
              fontWeight: 600,
              color: "#242426",
            }}
          >
            HK
          </span>
        </div>

        {/* Name Title */}
        <div style={{ position: "relative", display: "inline-block" }}>
          <h1
            style={{
              fontFamily: "'DM Serif Display', serif",
              fontSize: "clamp(44px, 8vw, 84px)",
              fontWeight: 400,
              lineHeight: 1.05,
              margin: 0,
              color: "#242426",
              letterSpacing: "-0.01em",
            }}
          >
            Huma Kiran
          </h1>
          {/* Hand-drawn Pen underline */}
          <svg
            viewBox="0 0 300 24"
            style={{
              display: "block",
              width: "100%",
              height: "18px",
              marginTop: "2px",
              overflow: "visible",
            }}
          >
            <path
              d="M 5 12 Q 75 4, 150 14 T 295 10"
              fill="none"
              stroke="#7d84ef"
              strokeWidth="3.2"
              strokeLinecap="round"
            />
          </svg>
        </div>

        {/* Hand-written tagline note */}
        <p
          style={{
            fontFamily: "'Caveat', cursive",
            fontSize: "clamp(22px, 3vw, 32px)",
            color: "#7d84ef",
            marginTop: "12px",
            marginBottom: 0,
            transform: "rotate(-1.5deg)",
          }}
        >
          crafting career journey & live projects...
        </p>
      </div>

      {/* Bottom Progress Bar & Counter */}
      <div
        className="preloader-content"
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "10px",
        }}
      >
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "baseline",
            width: "min(360px, 86vw)",
            fontSize: "14px",
            color: "rgba(36, 36, 38, 0.7)",
          }}
        >
          <span style={{ fontFamily: "'Caveat', cursive", fontSize: "20px", color: "#242426" }}>
            loading portfolio
          </span>
          <span
            style={{
              fontFamily: "'Poppins', sans-serif",
              fontWeight: 600,
              fontSize: "15px",
              letterSpacing: "0.05em",
              color: "#242426",
            }}
          >
            {percent}%
          </span>
        </div>

        {/* The Progress Track and Bar */}
        <div
          style={{
            width: "min(360px, 86vw)",
            height: "4px",
            background: "rgba(36, 36, 38, 0.12)",
            borderRadius: "99px",
            overflow: "hidden",
            position: "relative",
          }}
        >
          <div
            style={{
              width: `${percent}%`,
              height: "100%",
              background: "linear-gradient(90deg, #7d84ef 0%, #5d66eb 100%)",
              borderRadius: "99px",
              transition: "width 0.1s linear",
            }}
          />
        </div>
      </div>
    </div>
  )
}
