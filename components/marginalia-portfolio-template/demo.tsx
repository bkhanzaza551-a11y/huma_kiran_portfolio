"use client"

import MarginaliaPortfolioTemplate from "@/components/ui/marginalia-portfolio-template"

export default function Demo() {
  return (
    <MarginaliaPortfolioTemplate
      title="Huma Kiran"
      name="Portfolio"
      role="Software Engineer & Operations Lead"
      docLabel="Career Journey"
      portrait="/huma-kiran.jpg"
      cvUrl="/Huma-Kiran-Resume.pdf"
      cvNote="official resume (PDF)"
      signature="Huma Kiran"
      sections={["cover", "hello", "education", "skills", "projects", "facts", "thanks"]}
    />
  )
}
