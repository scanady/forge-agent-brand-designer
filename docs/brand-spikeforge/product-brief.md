# SpikeForge — Core Process Flows

> This document describes the day-to-day process flows for a coaching practice on SpikeForge, written from the perspective of each user role. The goal is to define how processes **should** flow to guide system design — not to document current implementation state.
>
> **Roles referenced throughout:**
> - **Visitor / Prospect** — An anonymous person exploring the practice's public site
> - **Client** — An active, enrolled participant in coaching services
> - **Coach** — An individual delivering coaching sessions to clients
> - **Practice Lead** — The operational manager who runs the practice day-to-day

---

## 1. Prospect Engagement & Discovery Call

This is the front door of the practice. A person discovers the coaching practice, explores what's offered, and decides whether to take the first step — scheduling a discovery call with the practice lead.

### 1.1 How a Prospect Finds the Practice

A prospect arrives at the practice's public website through one of several channels:

- **Direct referral** — A colleague, manager, or HR representative shares a link or recommends the practice by name.
- **Search** — The prospect finds the practice while searching for coaching services, leadership development, or related topics.
- **Manager endorsement** — A manager sends a direct recommendation with a link, often framed as an investment in the person's growth.
- **Social media / content** — The prospect encounters a coach's content (article, talk, post) and follows through to the practice site.

Once on the site, the prospect can freely explore without creating an account:

- **Practice overview** — What the practice does, who it serves, and the coaching philosophy.
- **Coach directory** — Browse coach profiles including bios, specialties, certifications, and areas of expertise. Each profile gives the prospect a sense of the coach's style and experience.
- **Services catalog** — View available coaching programs, packages, and session types with descriptions, durations, and pricing.
- **Testimonials and social proof** — Evidence that coaching works, framed around leaders and professionals who've invested in their growth.

> **Key principle:** The public site is designed to answer the prospect's unspoken questions — *"Is this for someone like me? What will I actually get? Can I trust these people?"* — without requiring any commitment.

### 1.2 Deciding to Schedule a Discovery Call

At some point the prospect decides to take the next step. The discovery call is positioned as a low-commitment, high-value conversation:

- **What it is:** A free 30-minute conversation with the practice lead to discuss the prospect's goals, challenges, and whether coaching is the right fit.
- **What it is not:** A sales pitch or obligation. The prospect can walk away at any time.

The call-to-action is accessible from multiple entry points across the site — the homepage, coach profiles, the services page, and a persistent "Schedule a Discovery Call" option. The intent is that no matter where the prospect is in their exploration, taking the next step is always one click away.

### 1.3 Scheduling the Discovery Call

The prospect selects "Schedule a Discovery Call" and enters a simple booking flow:

1. **Provide basic information** — Name, email, phone number, company, role. This is kept minimal to avoid friction.
2. **Share context** (optional) — A brief note about what they're looking for, what challenges they're facing, or what prompted them to explore coaching. This helps the practice lead prepare.
3. **Select a time** — The system displays available time slots based on the practice lead's calendar. The prospect chooses a date and time that works for them. Times are shown in the prospect's local timezone.
4. **Confirm the booking** — The prospect reviews their selection and confirms.

**What happens next:**

- The prospect receives a **confirmation email** with the date, time, and details of the discovery call. This includes a calendar invitation and a video meeting link (or location, for in-person calls).
- The prospect receives an **automated reminder** 24 hours before the call and another 1 hour before.
- The prospect can **reschedule or cancel** the call at any time before it occurs, with appropriate notice.

> **From the prospect's perspective:** Scheduling takes 2–3 minutes. They provide the minimum information needed, pick a time, and they're done. The system handles the rest — confirmations, reminders, and calendar logistics.

### 1.4 What the Practice Lead Sees

When a prospect books a discovery call, the practice lead is notified and the call appears in their discovery call pipeline:

- **New booking alert** — The practice lead sees the new call in their upcoming pipeline with the prospect's name, scheduled time, and any context the prospect provided.
- **Prospect background** — The practice lead can review the prospect's submitted information: name, company, role, coaching interests, and any notes.
- **Preparation workflow** — As the call approaches (within 48 hours), the system prompts the practice lead to prepare — review the prospect's background, check for prior interactions, and note any talking points.

### 1.5 The Discovery Call

The discovery call itself happens outside the system (via video call, phone, or in-person). It's a conversation, not a transaction. The practice lead's goals during the call are to:

- **Understand the prospect's situation** — What challenges are they facing? What are their goals? What's driving them to explore coaching now?
- **Explain the coaching approach** — How the practice works, what a coaching engagement looks like, and what kind of outcomes the prospect can expect.
- **Assess fit** — Is this person someone the practice can genuinely help? Is the timing right? Are expectations realistic?
- **Discuss next steps** — If it's a good fit, outline the path forward. If not, be honest about why and potentially suggest alternatives.

### 1.6 After the Discovery Call — Recording the Outcome

After the call, the practice lead records the outcome. This is a critical moment — it determines what happens next for the prospect. There are four possible outcomes:

#### Outcome A: Ready to Start
The prospect wants to move forward with coaching. The practice lead initiates the **client onboarding process** (see Section 2). The prospect's information carries forward — nothing needs to be re-entered. The practice lead may discuss initial program recommendations during or after the call.

#### Outcome B: Great Conversation — Follow Up Later
The prospect is interested but not ready to commit. Common reasons include timing (starting a new role, finishing a project), budget (waiting for approval or a new budget cycle), or simply needing more time to decide.

The practice lead:
- Records notes about the conversation and what the prospect is thinking.
- Sets a follow-up date — typically 1–2 weeks or 1 month out.
- The prospect stays in the system as an active lead.

When the follow-up date arrives, the system reminds the practice lead to re-engage. At that point, the practice lead reaches out and either:
- Books another discovery call to continue the conversation.
- Converts the prospect to a client if they're now ready.
- Closes the lead if they're no longer interested.

#### Outcome C: Not the Right Fit
The practice lead determines that coaching isn't the right solution for this person right now — or the prospect decides it's not for them. The practice lead records a brief reason (budget constraints, timing, looking for a different specialty, not ready for coaching) and the engagement ends gracefully. The prospect's record remains in the system in case they return in the future, but no active follow-up is scheduled.

#### Outcome D: No Show
The prospect didn't join the call. This happens. The practice lead can:
- **Send a rescheduling link** — An email goes to the prospect with a link to book a new time, no questions asked. Life gets busy; the tone is understanding, not punitive.
- **Mark as no-show and move on** — If the practice lead has reason to believe the prospect isn't engaged, they simply note the no-show. The prospect can always come back and schedule again on their own.

> **Key principle:** Every outcome has a clear next action. The practice lead never finishes a discovery call wondering "now what?" The system guides them to record, follow up, convert, or close — and tracks that it happened.

### 1.7 The Prospect's Experience After the Call

From the prospect's side, they either:

- **Receive an invitation to get started** — If the practice lead marked them as "Ready to Start," the prospect will receive communication about next steps for onboarding (see Section 2).
- **Hear back later** — If follow-up was selected, the prospect doesn't hear anything immediately, but the practice lead will re-engage at the agreed time.
- **Receive a graceful close** — If not the right fit, the prospect is thanked for their time. No awkward silence or ghosting.
- **Get a second chance to book** — If they no-showed, they receive a friendly email with a link to reschedule at their convenience.

---

## 2. Client Onboarding

Onboarding is the bridge between "I want to do this" and "I'm working with my coach." A well-run practice treats onboarding as a critical first impression — it sets the tone for the entire coaching relationship. Done well, the client feels welcomed, informed, and confident they made the right decision. Done poorly, buyer's remorse sets in before the first session.

### 2.1 Converting a Prospect to a Client

After a successful discovery call (Outcome A — Ready to Start), the practice lead converts the prospect into a client. This is an internal action that happens within the system:

1. **Initiate conversion** — The practice lead selects "Convert to Client" from the discovery call outcome flow. The prospect's information (name, email, phone, company, role) pre-populates the new client record. No re-entry required.
2. **Add onboarding context** — The practice lead captures key insights from the discovery call: the client's primary goals, challenges discussed, any specific preferences (e.g., coaching style, scheduling constraints), and recommended services. These notes become the foundation for the coaching engagement.
3. **Assign a coach** — The practice lead selects a coach for the client based on:
   - **Specialty alignment** — Does the coach have expertise relevant to the client's goals? A client navigating a C-suite transition needs a different coach than one building team management skills for the first time.
   - **Capacity** — Does the coach have room for another client? Overloading coaches degrades service quality. The system shows each coach's current workload.
   - **Style fit** — Based on what the practice lead learned during the discovery call, which coach's approach is most likely to resonate with this client?
   - If the practice lead is also the client's coach (common in smaller practices), they assign themselves.
4. **Select an initial service** — The practice lead recommends or enrolls the client in their first coaching service — a program, package, or initial ad-hoc session. This may have been discussed during the discovery call, or the practice lead may recommend based on the client's situation.

> **Best practice:** Don't delay the coach assignment. The longer a new client waits without a named coach, the more momentum fades. Ideally, the client hears "You'll be working with [Coach Name]" within 24 hours of saying yes.

### 2.2 The Welcome Experience

Once the conversion is complete, the client receives a **welcome email** — the first official communication as a client of the practice. This email sets expectations and makes the next step clear:

- **A warm welcome** — Acknowledging their decision and reinforcing that they've made a great choice. Tone matters here — professional but human.
- **Their coach introduction** — Who their coach is, a brief note about why they were matched, and a link to the coach's profile. If the practice lead discussed the coach during the discovery call, this reinforces that conversation.
- **Account setup instructions** — A secure link to create their password and access the client portal. The account is pre-created with their email — they just need to set a password.
- **What to expect next** — A clear description of what happens from here: "Your coach will reach out within [X] days to schedule your first session. In the meantime, you can explore your portal and review your coaching program."

> **Best practice:** The welcome email should arrive within hours of the conversion, not days. Speed signals professionalism and keeps the client's enthusiasm high. In a well-run practice, the prospect goes from "I'm ready" to "I have an account and know my coach's name" the same day.

### 2.3 Client Account Setup

The client clicks the link in their welcome email and sets up their account:

1. **Set a password** — Simple, secure password creation. The account email is already confirmed from the discovery call booking.
2. **Complete their profile** — The client fills in any additional details: contact preferences, timezone (confirmed from location), and a brief self-description of their goals. This is kept light — the deep goal-setting happens with their coach.
3. **Verify email** — If not already verified, the client confirms their email address.

Once complete, the client lands in their **client portal** — a clean dashboard showing:
- Their assigned coach's name and photo.
- Their active program or package.
- A prompt to book their first session (or a note that their coach will be in touch).
- A welcome message or getting-started guide.

### 2.4 The Coach's Onboarding Role

When a new client is assigned to a coach, the coach receives a notification with the client's background:

- **Client context** — The notes from the discovery call, the client's stated goals, company, role, and any preferences the practice lead recorded.
- **Recommended service** — What program or package the client was enrolled in.
- **Action prompt** — The coach is prompted to reach out to the client within a defined timeframe (e.g., 48 hours) to introduce themselves and schedule the first session.

The coach's first outreach sets the tone for the relationship. Best practices for this initial contact:

- **Personal, not templated** — Reference something specific from the discovery call notes. "I understand you're navigating a transition into a VP role — I've worked with several leaders through similar transitions and I'm looking forward to our work together."
- **Set expectations** — Briefly explain how sessions will work, the typical cadence, and what the client should bring to the first session.
- **Schedule the first session** — Offer specific time slots or direct the client to the booking system. Don't leave scheduling open-ended — "find a time that works" creates unnecessary friction.

> **Best practice:** The first session should happen within 1–2 weeks of onboarding. Research consistently shows that the longer the gap between commitment and first session, the higher the drop-off rate. Momentum matters.

### 2.5 The Intake Session (First Coaching Session)

The first session is different from all sessions that follow. It's not a coaching session in the traditional sense — it's a structured intake designed to build the foundation for the engagement:

- **Build rapport** — The coach and client get to know each other as people, not just roles. Trust is the currency of coaching; this is where it starts.
- **Clarify goals** — The coach works with the client to define 2–3 specific, measurable coaching goals. What does success look like in 3 months? 6 months? These goals become the North Star for every session.
- **Establish the coaching agreement** — How will sessions work? What's the cadence (typically bi-weekly for executive coaching)? What's expected between sessions? How will progress be measured? What are the ground rules for confidentiality?
- **Assess the starting point** — Where is the client today relative to their goals? This baseline makes progress visible over time. Some practices use a brief self-assessment or 360-degree feedback tool; others rely on the coaching conversation.
- **Agree on the first action** — The client leaves the intake session with at least one concrete action to take before the next session. This establishes the pattern: coaching is not something that happens *to* you in a session — it's something you do *between* sessions.

The coach records the agreed-upon goals, the coaching cadence, and any notes from the intake in the system. These become visible to the practice lead (for oversight) and to the client (for reference).

> **Best practice:** Never skip goal-setting. Coaching without clear goals drifts into pleasant conversation. Goals give every session purpose and give the client a way to see their own progress. Revisit goals at the midpoint of the engagement to check alignment.

### 2.6 Onboarding Timeline Summary

A well-run onboarding follows this rhythm:

| Milestone | Timing | Owner |
|---|---|---|
| Discovery call completed, outcome recorded | Day 0 | Practice Lead |
| Prospect converted to client, coach assigned | Within 24 hours | Practice Lead |
| Welcome email sent with account setup link | Same day as conversion | System (automatic) |
| Client creates account and accesses portal | Within 1–3 days | Client |
| Coach sends personal introduction and scheduling link | Within 48 hours of assignment | Coach |
| First session (intake) scheduled | Within 1–2 weeks of onboarding | Coach + Client |
| Goals established, coaching cadence set | During first session | Coach + Client |

---

## 3. Coaching Engagement & Session Management

This is the core of the practice — the ongoing rhythm of coaching sessions where the real work happens. A well-managed session cadence keeps clients engaged, coaches effective, and the practice running smoothly.

### 3.1 Session Cadence and Scheduling

Once the intake session establishes the coaching cadence, sessions follow a regular rhythm. The standard in executive coaching is:

- **Bi-weekly sessions** — Every two weeks is the most common cadence for executive coaching. It gives clients enough time to apply what they discussed, reflect, and bring new observations to the next session.
- **Weekly sessions** — Used for intensive engagements, onboarding coaching (first 90 days in a new role), or when a client is working through a time-sensitive challenge.
- **Monthly sessions** — Used for maintenance engagements, experienced leaders who need a periodic sounding board, or as a step-down from a more intensive program.

**How scheduling works:**

1. **Client books sessions** — Clients schedule sessions through their portal based on their coach's published availability. The system shows available times in the client's timezone.
2. **Recurring booking** — For established cadences, clients can book recurring sessions (e.g., every other Tuesday at 10am) so they don't have to manually book each time. Recurring sessions appear on both the client's and coach's calendars.
3. **Minimum notice** — Sessions require advance booking notice (e.g., 24–48 hours) to give the coach time to prepare. Last-minute bookings create unprepared sessions and lower quality.
4. **Session duration** — Typical executive coaching sessions are 60 minutes. Some formats use 45 or 90 minutes depending on the program. The session duration is set by the service type.

**Calendar integration:**

- Both client and coach receive calendar invitations with video meeting links for every scheduled session.
- Automated reminders go out 24 hours and 1 hour before each session.
- Calendar events update automatically when sessions are rescheduled.

> **Best practice:** Encourage clients to book their next session before ending the current one. "Same time in two weeks?" takes 10 seconds and prevents scheduling gaps that break momentum. The system should make rebooking frictionless.

### 3.2 Before the Session — Preparation

Effective coaching sessions don't start when the video call connects. They start with preparation:

**For the coach:**
- **Review previous session notes** — What was discussed? What actions did the client commit to? What themes are emerging?
- **Check client goals** — Are the session topics tracking toward the client's stated coaching goals, or has the conversation drifted?
- **Prepare questions or frameworks** — What's the most useful thing the coach can bring to this session based on where the client is?

**For the client:**
- **Reflect on progress** — What happened since the last session? Did they follow through on their commitments? What surprised them?
- **Identify a focus** — What's the most important thing to work on today? Clients who arrive with a topic get more from their sessions than those who wait for the coach to lead.

> **Best practice:** The system can support preparation by surfacing the previous session's notes and action items to both the coach and client before the next session. A simple "What would you like to focus on today?" prompt sent to the client 24 hours before the session gives the coach valuable context.

### 3.3 During the Session

The session itself happens outside the system (video call, phone, or in-person). While every coach has their own style, effective coaching sessions generally follow a structure:

1. **Check-in** (5 minutes) — How is the client doing? What's top of mind? A quick pulse on energy and focus.
2. **Review commitments** (5–10 minutes) — What actions did the client take since the last session? What worked? What didn't? This builds accountability into the coaching relationship.
3. **Deep work** (35–40 minutes) — The core of the session. Coach and client explore the topic the client brought, using questioning, reflection, frameworks, role-play, or whatever approach fits. The coach's job is to help the client think more clearly, see blind spots, and develop their own solutions.
4. **Action and commitment** (5–10 minutes) — What will the client do between now and the next session? Specific, concrete, and owned by the client. "I'll think about it" is not an action item. "I'll have a direct conversation with my VP about role clarity by Friday" is.

### 3.4 After the Session — Documentation

Within 24 hours of the session, the coach records session notes in the system:

- **Session summary** — A brief capture of what was discussed, key insights, and themes.
- **Action items** — What the client committed to doing before the next session.
- **Progress observations** — How is the client tracking against their coaching goals? Any shifts in focus or new challenges emerging?
- **Session status** — Marked as completed, which automatically deducts from the client's package or program balance.

These notes serve multiple purposes:
- **For the coach:** Continuity between sessions. No coach can remember every detail across multiple clients. Notes make the next session's preparation effortless.
- **For the client:** Clients can view a summary of their session in the portal, reinforcing what they discussed and keeping action items visible.
- **For the practice lead:** Session documentation provides evidence that sessions are happening, that clients are progressing, and that coaching quality is being maintained.

> **Best practice:** Notes should be recorded the same day as the session while the conversation is fresh. Brief but specific — 3–5 bullet points, not a transcript. The goal is to capture what matters, not everything that was said.

### 3.5 Rescheduling and Cancellations

Life happens. Sessions get rescheduled. A clear, fair policy keeps the practice professional and respects everyone's time:

- **Client rescheduling** — Clients can reschedule sessions with minimum notice (e.g., 24 hours). The system makes rebooking easy — the client picks a new time from the coach's availability.
- **Late cancellation** — Cancellations within the notice window (e.g., less than 24 hours before the session) may count as a completed session against the client's package balance, per the practice's cancellation policy. This policy is communicated during onboarding so there are no surprises.
- **Coach rescheduling** — Coaches can reschedule sessions when needed, with the client notified automatically. The tone is professional — "Your coach needs to reschedule your session on [date]. Please select a new time." Coaches should reschedule rarely; frequent rescheduling erodes client trust.
- **No-shows** — If a client doesn't join a session, the coach waits 10–15 minutes, then marks the session as a no-show. The system can automatically send a "We missed you" message with a rebooking link. Repeated no-shows are a red flag the coach should discuss with the client — and potentially escalate to the practice lead.

> **Best practice:** Track cancellation and no-show rates per client. A pattern of cancellations often signals a client who is disengaging, overwhelmed, or not getting value from coaching. The coach should address this directly with the client rather than waiting for the problem to worsen. Early intervention saves the engagement.

### 3.6 Session Tracking and Visibility

Every session is tracked across its lifecycle: **scheduled → completed / cancelled / no-show.** All parties have visibility:

- **Client** sees: Upcoming sessions, past sessions with notes, action items, sessions remaining in their package or program.
- **Coach** sees: Their full session calendar across all clients, session history per client, notes, and action items.
- **Practice Lead** sees: Session activity across the practice — which coaches are delivering sessions, which clients are active, cancellation rates, and overall utilization.

---

## 4. Coach Management of Client Engagement

This section describes the coach's day-to-day workflow — how they manage their roster of clients, stay prepared, maintain quality, and flag issues before they become problems.

### 4.1 The Coach's Dashboard

When a coach logs in, their dashboard is a command center for their practice. It shows the information they need to manage their day and their clients:

- **Today's sessions** — What's on the calendar today, with quick links to preparation notes and client context.
- **Upcoming sessions this week** — A look-ahead so the coach can prepare in advance.
- **Action items to address** — Clients with overdue follow-ups, sessions without notes recorded, or preparation needed for upcoming calls.
- **Client roster summary** — Total active clients, capacity remaining, and any clients flagged for attention.
- **Discovery call pipeline** — Upcoming and pending discovery calls (if the coach handles them).

The dashboard is designed around a simple principle: **the coach should never have to hunt for what needs their attention next.** The system surfaces the most urgent and important items automatically.

### 4.2 Managing the Client Roster

Each coach maintains a roster of active clients. For each client, the coach can see:

- **Client profile** — Name, company, role, contact details, and coaching goals (established during the intake session).
- **Engagement details** — What service they're enrolled in, how many sessions are completed vs. remaining, start date, and expected end date.
- **Session history** — A chronological record of all sessions: dates, notes, action items, and outcomes.
- **Progress toward goals** — How the client is tracking against the goals set during intake. This is qualitative, informed by the coach's observations and the client's self-reported progress.

> **Best practice:** Review each client's status at least once per week, even clients you're not seeing that week. A quick scan of session frequency, outstanding action items, and goal progress helps you catch disengagement early. If a client hasn't scheduled their next session, reach out proactively — don't wait for them.

### 4.3 Client Health and Engagement Signals

Not every client will tell you when something isn't working. The system and the coach should watch for signals:

**Positive engagement signals:**
- Sessions are booked consistently, on cadence.
- Client arrives prepared with topics and reflections.
- Action items are completed or meaningfully attempted between sessions.
- Client proactively reaches out between sessions with questions or updates.

**Warning signals:**
- Missed or cancelled sessions, especially 2+ in a row.
- Sessions booked but frequently rescheduled.
- Client consistently arrives without a topic or preparation.
- Action items are not completed, and the pattern repeats.
- Client seems disengaged during sessions — going through the motions.

When a coach identifies warning signals, the appropriate response depends on the situation:

1. **Address it directly with the client** — "I've noticed we've been rescheduling frequently. I want to make sure coaching is still serving you well. What's going on?" This is a coaching conversation, not an accusation.
2. **Adjust the approach** — Maybe the cadence is wrong, the goals need updating, or the coaching style isn't clicking. Flexibility is a strength, not a weakness.
3. **Involve the practice lead** — If the pattern continues or the client is unresponsive, the coach raises it with the practice lead. The practice lead may reach out to the client directly, suggest a coach reassignment, or discuss whether the engagement should be paused or concluded.

> **Best practice:** The practice lead should have a standing check-in with each coach — weekly or bi-weekly — to review the client roster. This isn't micromanagement; it's quality assurance. A 15-minute conversation catches issues that would otherwise go unnoticed until a client quietly disengages.

### 4.4 Between-Session Client Communication

Coaching doesn't only happen in sessions. How the coach communicates between sessions shapes the client's experience:

- **Session follow-up** — A brief message after a session reinforcing key takeaways or encouraging the client on their action items. Not required for every session, but powerful when used intentionally.
- **Resource sharing** — Articles, frameworks, book recommendations, or exercises relevant to what the client is working on. The coach is a curator of relevant insights.
- **Check-ins** — A short note midway between sessions: "How did the conversation with your leadership team go?" Shows the coach is invested and keeps the client accountable.
- **Availability** — Clients should know they can reach their coach between sessions for brief questions or to share a win. Boundaries are important (coaching is not therapy, and coaches are not on-call), but reasonable accessibility builds trust.

All in-portal communication is logged and visible to the practice lead, supporting both transparency and continuity if a coach transition ever becomes necessary.

> **Best practice:** The most effective coaches maintain a light but consistent presence between sessions. The worst thing a client can feel between sessions is "my coach forgets about me until the next call." Even a two-sentence message every couple of weeks signals attentiveness.

### 4.5 Session Notes and Continuity

Session notes are not administrative overhead — they are the backbone of continuity and quality:

- **Record notes the same day** — Within 24 hours of the session, ideally within a few hours. Waiting until the end of the week degrades accuracy.
- **Capture the right level of detail** — Key themes discussed, client insights or breakthroughs, action items committed to, and any shifts in goals or focus. Not a transcript; a meaningful summary.
- **Link to goals** — Periodically note how the session connected to the client's stated coaching goals. This creates a narrative of progress that's invaluable during midpoint and end-of-engagement reviews.

The system tracks whether session notes have been recorded and flags sessions without notes. The practice lead monitors this as part of quality management.

> **Best practice:** If a coach has to be away (vacation, illness) or a client needs to be reassigned to a new coach, thorough session notes are what make the transition possible without the client having to "start over." Notes are an act of professionalism, not bureaucracy.

### 4.6 Coach Capacity Management

Each coach has a defined capacity — the maximum number of active clients they can serve effectively. This is not just about calendar hours; it's about the cognitive and emotional bandwidth required to coach well:

- **The practice lead sets capacity** based on the coach's experience, availability, and the complexity of their client engagements.
- **The system tracks current workload** — active clients, sessions per week, and utilization rate.
- **The system alerts** when a coach approaches capacity, preventing over-assignment.

When a coach is at capacity, the practice lead either holds new client assignments until a slot opens or assigns to another coach.

> **Best practice:** A common mistake in growing practices is overloading top coaches because they're good and clients like them. This leads to burnout, lower session quality, and eventually coach turnover. Protect capacity limits. A fully-booked coach should trigger growth conversations (hiring another coach), not more assignments.

---

## 5. Program & Package Lifecycle

Services are the structure around which coaching engagements are organized. They define what a client is getting, how many sessions, over what timeframe, and at what cost. A well-designed service catalog makes it easy for clients to understand their options and for the practice to deliver consistently.

### 5.1 How the Practice Designs Services

The practice lead creates and manages the service catalog. There are three core service types:

**Predefined Programs:**
Structured coaching engagements with a defined arc — a set number of sessions over a defined time period, often with milestones.

- Example: *"Executive Leadership Accelerator — 12 sessions over 6 months, bi-weekly cadence. Includes intake assessment, midpoint review, and completion summary."*
- Programs are designed around specific outcomes (leadership transition, executive presence, team effectiveness) and target specific audiences.
- Programs may include a mix of 1:1 coaching sessions, assessments, and between-session exercises.

**Session Packages:**
A bundle of sessions that the client can use flexibly within a validity period.

- Example: *"10-Session Coaching Package — Use within 6 months. Book sessions at your pace."*
- Packages give clients flexibility to schedule sessions when they need them rather than following a fixed cadence.
- The system tracks how many sessions have been used and how many remain, and alerts the client and coach when the package is nearing depletion.

**Ad-Hoc Sessions:**
Individual sessions purchased one at a time for clients who want coaching without a longer commitment.

- Example: *"Single Coaching Session — 60 minutes, $350."*
- Often used for one-off needs (preparing for a board presentation, navigating a specific conflict) or as a try-before-you-commit entry point.
- Payment is collected before the session is scheduled.

> **Best practice:** A well-designed catalog has 3–5 core offerings, not 15. Too many options create decision paralysis for clients and operational complexity for the practice. Keep it simple: one or two programs for different audiences, a flexible package, and an ad-hoc option. You can always create a custom engagement for a client with unique needs.

### 5.2 Client Enrollment

Enrollment is how a client begins a specific service. It can happen in two ways:

**Practice-led enrollment (most common):**
The practice lead enrolls the client in a service during or after onboarding. This is the typical path — the practice lead recommends a program or package based on the discovery call conversation, and the client agrees.

1. Practice lead selects the service and the client.
2. System creates the enrollment record with start date, session count, and expected timeline.
3. If payment is required upfront, the enrollment triggers a payment request (see Section 6).
4. Client and coach are both notified: the client sees their new enrollment in their portal, and the coach sees it in their client's engagement details.

**Client self-enrollment (future):**
For established clients or in marketplace scenarios, clients browse the catalog and enroll themselves.

1. Client selects a service from the catalog.
2. Client reviews the terms, pricing, and commitment.
3. Client completes payment.
4. Enrollment is activated and the practice lead is notified.

### 5.3 The Active Engagement

Once enrolled, the engagement follows its natural arc:

**For programs (structured):**

- **Kickoff** — The intake session (described in Section 2.5) serves as the program kickoff. Goals are set, cadence is agreed upon, and the timeline is established.
- **Regular sessions** — Sessions happen on cadence. The system tracks sessions completed vs. total. Both client and coach can see progress.
- **Midpoint review** — At the halfway mark, the coach and client revisit goals. Are they on track? Do goals need adjusting? Is the coaching approach working? The midpoint is a checkpoint, not a formality — it's where engagements are saved or sharpened.
- **Completion approach** — As the end of the program nears, the coach begins the closure conversation: What's been achieved? What's different now? What still needs attention? What will the client do on their own going forward?
- **Completion** — The final session wraps the engagement. The coach records a completion summary: goals achieved, key growth areas, and recommendations for continued development. The practice lead reviews the completion.

**For packages (flexible):**

- **Usage tracking** — Each session deducts from the package balance. The system shows remaining sessions prominently for both the client and coach.
- **Depletion alerts** — When a package is approaching zero (e.g., 2 sessions remaining), the system notifies the client and coach. The coach can discuss re-enrollment or transition options during their next session.
- **Expiration** — Packages have a validity period. As the expiration date approaches (e.g., 30 days out), the system alerts the client. Unused sessions after expiration are forfeited per the package terms — this policy is communicated at enrollment.

### 5.4 Program Completion and What Comes Next

When an engagement concludes, the practice doesn't just close a record — this is a moment for reflection and continuity:

- **Completion summary** — The coach records a final summary of the engagement: goals at the start, progress made, outcomes achieved, and any recommendations. This becomes part of the client's permanent record.
- **Client feedback** — The client is invited to provide feedback on their experience: the coaching quality, the program structure, and the overall value. This feedback goes to the practice lead and helps improve the practice.
- **Next steps conversation** — Not every client needs to re-enroll, but every client deserves a thoughtful transition:
  - **Re-enrollment** — The client wants to continue. The coach and client discuss the next engagement: same format or different? New goals? The practice lead facilitates the new enrollment.
  - **Step-down** — The client moves from a structured program to a lighter-touch package or monthly check-in. This maintains the relationship without the full commitment.
  - **Graduation** — The client has achieved what they set out to do. The coach celebrates the progress, reinforces the client's ability to continue on their own, and leaves the door open for future engagement. "When you need a sounding board, we're here."
  - **Referral** — The client's needs have evolved beyond what the practice offers (e.g., they need career counseling, therapy, or a different coaching specialty). The coach or practice lead provides a thoughtful referral.

> **Best practice:** Never let an engagement end in silence. A proper conclusion — even if the client doesn't re-enroll — is what separates a professional practice from a transactional one. Clients who feel well-served at the end of an engagement become the practice's best source of referrals.

### 5.5 The Practice Lead's Role in Service Lifecycle

The practice lead oversees the health of all active engagements across the practice:

- **Enrollment monitoring** — Which clients are active? Which are approaching completion? Are there clients whose packages are about to expire unused?
- **Utilization tracking** — Are programs being fully utilized? If clients consistently use only 8 of 12 sessions in a program, the program design may need adjustment.
- **Coach assignment balance** — Are client engagements distributed reasonably across coaches? Is any coach carrying a disproportionate load?
- **Revenue pipeline** — Upcoming expirations and completions represent renewal opportunities. The practice lead should proactively plan for these conversations rather than reacting when clients ask "what now?"

---

## 6. Payment for Services

Payment is the necessary business side of coaching. A well-run practice handles money cleanly, transparently, and without making it awkward — for the client or the practice. The goal is to make payment a smooth, expected step in the process rather than a source of friction.

### 6.1 Pricing Philosophy

How pricing is structured affects how clients perceive value:

- **Pricing is transparent** — Service prices are visible in the catalog. Clients should never have to ask "how much does this cost?" Opacity breeds distrust; transparency builds confidence.
- **Pricing reflects value, not just time** — A 12-session leadership program isn't priced as "12 × hourly rate." It's priced for the outcome: a more effective leader. The catalog descriptions, session counts, and pricing should reinforce that the client is investing in a transformation, not buying hours.
- **Custom pricing is handled gracefully** — For enterprise clients, multi-person engagements, or special circumstances, the practice lead can apply custom pricing to an individual enrollment. Custom pricing doesn't appear in the public catalog — it's negotiated and applied at the engagement level.

### 6.2 When Payment Happens

Payment timing depends on the service type:

**Programs and Packages — Payment at enrollment:**
- When a client is enrolled in a program or package, a payment request is generated.
- Full payment is collected before the engagement begins or at the time of enrollment.
- The system generates an invoice and sends it to the client.
- Once payment is confirmed, the enrollment is activated and sessions become available for booking.
- If the practice offers payment plans (e.g., monthly installments for a 6-month program), the system manages the payment schedule and tracks each installment.

**Ad-hoc sessions — Payment before scheduling:**
- For single sessions, payment is collected at the time of booking.
- The client selects a session, provides payment, and then schedules the session.
- No scheduling without confirmed payment — this protects the coach's time and the practice's revenue.

**Subscription / recurring billing (future):**
- For clients on ongoing retainers or recurring packages, the system bills automatically on a set cycle (monthly, quarterly).
- Clients can manage their payment method and view upcoming charges in their portal.

> **Best practice:** Never let a client attend sessions on a balance they haven't paid. This seems obvious, but practices that "we'll sort out the billing later" create uncomfortable collection situations that damage relationships. Payment at enrollment or before the session keeps things clean.

### 6.3 The Client's Payment Experience

From the client's perspective, payment should feel like a simple, expected part of the process — not an obstacle:

1. **Clear pricing before commitment** — The client knows exactly what they're paying before they enroll. No hidden fees, no surprise charges.
2. **Secure payment processing** — Payment is processed through a trusted payment provider (e.g., Stripe). The system never stores raw credit card numbers. The client enters their payment information once and can reuse it for future purchases.
3. **Immediate confirmation** — After payment, the client receives a receipt via email and the payment appears in their portal's payment history.
4. **Easy access to records** — Clients can view all their payments, invoices, and receipts in one place within their portal. Many clients expense coaching or have their organization reimburse them — making records easily accessible is important.

### 6.4 Handling Payment Issues

Things don't always go smoothly. The practice should have clear processes for common payment situations:

- **Failed payment** — If a payment fails (declined card, insufficient funds), the system notifies the client and the practice lead. The enrollment is not activated until payment succeeds. The client receives a clear message about what to do (update payment method, contact their bank).
- **Refund requests** — The practice lead manages refunds according to the practice's refund policy. Common policy: full refund if requested before the first session; prorated refund based on sessions used; no refund after a defined point. The refund policy is communicated during enrollment. The system processes the refund and updates the client's records.
- **Payment disputes** — If a client disputes a charge, the practice lead handles it directly. The payment processor provides dispute resolution tools. Good documentation (signed agreements, session records, communication history) protects the practice.

> **Best practice:** Have a written refund and cancellation policy. Communicate it during onboarding, include it in the enrollment terms, and make sure coaches know it too. Most disputes arise from unclear expectations, not bad intentions. A clear policy prevents 90% of payment conflicts before they start.

### 6.5 Practice Financial Management

The practice lead manages the financial health of the practice through the system:

- **Revenue tracking** — Total revenue by time period (month, quarter, year), broken down by service type, coach, and client.
- **Outstanding invoices** — Any unpaid enrollment fees or overdue payment plan installments.
- **Upcoming revenue** — Enrollments that are about to start, packages about to renew, and the pipeline of prospects expected to convert.
- **Coach-level revenue** — Revenue associated with each coach's clients, supporting compensation decisions and performance tracking.
- **Payment history** — A complete, auditable record of all transactions: payments, refunds, and adjustments.

> **Best practice:** Review financial reports at least monthly. Look for trends: Is revenue growing? Are certain services more popular than others? Is there seasonal variation? Which coaches are generating the most client value? Financial data tells you what's working in your practice — but only if you look at it regularly.

---

## 7. Coach Onboarding to the Practice

Before a coach can serve clients, they need to be brought into the practice with intention. Hiring a good coach is one thing — integrating them so they can deliver consistently within the practice's standards is another. A structured onboarding process protects the practice's reputation and sets every coach up for success.

### 7.1 Vetting and Credentialing

Not every coach is a fit for every practice. Before onboarding begins, the practice lead evaluates the coach against the practice's standards:

- **Credentials** — What certifications does the coach hold? ICF credentials (ACC, PCC, MCC) are the industry standard for professional coaching. The practice should define its minimum credentialing requirement and verify it before proceeding.
- **Experience and specialization** — What populations has the coach served? What industries, role levels, and coaching domains do they cover? The goal is to add capability the practice needs — not duplicate what's already there.
- **Coaching philosophy and approach** — Does this coach's style align with the practice's methodology? A practice built around accountability-driven leadership coaching needs coaches who share that orientation. Philosophical misalignment creates an inconsistent client experience.
- **References and track record** — What do former clients or colleagues say? Can the coach provide evidence of successful engagements, client outcomes, or professional development?
- **Cultural fit** — Does this person operate professionally? Are they responsive, reliable, and coachable themselves? The practice is trusting them with client relationships.

> **Best practice:** Document your minimum requirements — don't assess coaches ad hoc. Write down what credentials, experience, and qualities a coach needs to join the practice. This makes hiring consistent and prevents lowering the bar when you're eager to grow.

### 7.2 Platform Setup

Once the practice lead decides to bring a coach on, their platform presence needs to be established:

1. **Create the coach account** — The practice lead creates the coach's account in the system and assigns the coach role.
2. **Build the profile** — The coach completes their profile: bio, photo, specialties, certifications, education, speaking engagements, publications, social links, and other professional details. The profile is the coach's public face — it should be polished and authentic.
3. **Configure availability** — The coach sets up their availability calendar: which days and times they're available for sessions and discovery calls, timezone, and any recurring blocks. Getting this right upfront prevents scheduling friction later.
4. **Assign services** — The practice lead determines which services the coach is qualified and authorized to deliver. Not every coach delivers every program. Matching coaches to services they're genuinely equipped for maintains quality.
5. **Set capacity** — The practice lead sets the coach's maximum client load based on their availability, experience level, and the intensity of the services they deliver.

### 7.3 Practice Orientation

Platform access is not the same as readiness. The coach needs to understand how the practice operates:

- **Practice methodology** — How does this practice approach coaching? What frameworks, assessments, or models are used? What does a typical engagement arc look like? Even experienced coaches need to learn the practice's specific approach.
- **Client experience standards** — What does the practice promise clients? Response time expectations, session preparation standards, note-taking requirements, communication norms between sessions. These aren't optional — they're the baseline for consistent quality.
- **System walkthrough** — How to use the platform: managing their calendar, preparing for discovery calls, recording session notes, tracking client progress, handling outcomes. A coach who fumbles the tools creates friction for clients.
- **Policies and boundaries** — Cancellation policies, confidentiality standards, escalation protocols, what to do when a session surfaces non-coaching concerns. The coach needs to know the rules before they're in a situation that requires them.
- **Introduction to the team** — Meet the practice lead, any other coaches, and understand the communication rhythm (standing check-ins, how to raise concerns, where to go for support).

> **Best practice:** Pair a new coach with an experienced coach in the practice for their first 2–3 client engagements. This isn't supervision — it's mentorship. A quick debrief after early sessions ("How did it go? Anything you weren't sure how to handle?") accelerates confidence and catches issues early. The investment is small; the payoff in quality is significant.

### 7.4 Ramp-Up Period

A new coach shouldn't go from zero to a full roster overnight:

- **Start with a limited load** — Assign 2–3 clients initially, regardless of the coach's overall capacity. This gives the practice lead time to assess how the coach operates within the practice's framework before scaling up.
- **Early feedback loop** — The practice lead checks in with the coach more frequently during the first month — weekly rather than bi-weekly. How are sessions going? Any questions about the methodology? Any client situations they want to talk through?
- **Client feedback** — After the new coach's first few engagements, gather informal client feedback. Are clients satisfied? Did the sessions meet expectations? This isn't a formal review — it's a quality check.
- **Full integration** — Once the practice lead is confident the coach is delivering consistently, they increase the client load toward full capacity.

### 7.5 Coach Onboarding Timeline

| Milestone | Timing | Owner |
|---|---|---|
| Vetting and credentialing complete | Before onboarding begins | Practice Lead |
| Account created, coach role assigned | Day 1 | Practice Lead |
| Profile completed and reviewed | Within 1 week | Coach + Practice Lead |
| Availability configured | Within 1 week | Coach |
| Practice orientation completed | Within first 2 weeks | Practice Lead |
| First client assigned | After orientation complete | Practice Lead |
| Ramp-up check-ins (weekly) | First 4–6 weeks | Practice Lead + Coach |
| Full capacity reached | 2–3 months | Practice Lead |

---

## 8. Client-Coach Reassignment & Transition

Sometimes a coaching relationship needs to change. The coach leaves the practice, goes on extended leave, the client requests a different coach, or the practice lead identifies a mismatch. This is one of the most sensitive processes in a practice. Handled poorly, you lose the client. Handled well, it can actually deepen trust — the client sees that the practice prioritizes their experience above any single relationship.

### 8.1 When Reassignment Happens

Reassignment is triggered by several scenarios, each requiring a different tone and approach:

**Coach-initiated:**
- **Coach departure** — The coach is leaving the practice (new opportunity, retirement, personal reasons). This is typically planned with lead time.
- **Extended leave** — The coach needs time away (medical, family, sabbatical) and their clients can't wait for them to return.
- **Capacity adjustment** — The coach is overloaded and the practice lead needs to redistribute clients to maintain quality.

**Client-initiated:**
- **Mismatch request** — The client doesn't feel the coaching relationship is working and asks for a different coach. This requires sensitivity — the request is valid, not a failure.
- **Changed needs** — The client's goals have evolved (e.g., from leadership transition to team development) and a different coach is better suited for the new focus area.

**Practice-lead-initiated:**
- **Quality concern** — The practice lead observes patterns (poor session documentation, client feedback, disengagement) that warrant a change.
- **Strategic rebalancing** — As the practice grows or evolves, client assignments may need to shift to better utilize the coaching team.

### 8.2 The Transition Process

Regardless of the trigger, the process follows the same structure:

1. **Decision and planning** — The practice lead decides that a reassignment is warranted. They select the new coach based on the same criteria used for initial assignment: specialty fit, capacity, and style compatibility with the client.

2. **Communicate with the outgoing coach** — If the coach is still with the practice, the practice lead discusses the transition respectfully. The outgoing coach prepares a handoff summary: client goals, progress to date, engagement history, any sensitivities, and recommendations for the next coach. This summary is critical — it's what prevents the client from having to "start over."

3. **Communicate with the client** — The practice lead (not the coach) informs the client about the change. The message should be:
   - **Honest about the reason** — "Coach [Name] is transitioning out of the practice, and we want to make sure your coaching continues without interruption." Or: "Based on where your goals have evolved, I think Coach [Name] is a stronger fit for the next phase of your work."
   - **Reassuring about continuity** — "Your new coach has reviewed your engagement history and goals. You won't have to repeat anything."
   - **Empowering the client** — "If this doesn't feel like the right fit after a session or two, tell me. We'll make it right."

4. **New coach preparation** — The incoming coach reviews the handoff summary, session history, client goals, and any relevant notes before the first session. They should arrive informed, not starting from scratch.

5. **Transition session** — The first session with the new coach is treated as a soft intake: acknowledge the transition, affirm the client's goals (or update them), establish rapport, and set expectations for the new relationship. It is not a full re-intake — the client's history and progress are honored.

6. **Follow-up** — The practice lead checks in with the client after the first 2–3 sessions with the new coach. "How is it going? Is the new partnership working for you?" This closes the loop and catches problems before they calcify.

> **Best practice:** Never surprise a client with a new coach. Even when the timeline is compressed (e.g., a coach leaves abruptly), the practice lead should contact the client before their next session to explain what's happening. Silence or a surprise new face on a video call destroys trust instantly.

### 8.3 When a Client Requests a Change

This deserves special attention because it requires emotional intelligence:

- **Listen without defensiveness** — The client's perception is valid. Maybe the styles don't click, the coach's approach isn't resonating, or the client simply needs something different. None of these are failures.
- **Don't investigate blame** — The goal is to solve the problem, not determine who's at fault. Ask the client what they're looking for in a coach so you can match them better.
- **Move quickly** — A client who asks for a change has already been thinking about it for a while. Delays increase the chance they disengage entirely.
- **Inform the outgoing coach professionally** — The coach needs to know, and they need to hear it without judgment. "The client has asked for a different match. This happens. Let's make the transition smooth."

> **Best practice:** Track reassignment frequency per coach. One reassignment is normal. A pattern of multiple clients requesting changes from the same coach is a signal that needs attention — not punishment, but a conversation about coaching approach, client experience, or fit for the practice.

---

## 9. Client Disengagement & Exit (Mid-Engagement)

Not every coaching engagement reaches its planned conclusion. Clients stop for all kinds of reasons — some within the practice's control, some not. How the practice handles these situations defines its professionalism and determines whether the relationship ends permanently or pauses with the door left open.

### 9.1 Types of Mid-Engagement Exit

**Client-initiated:**
- **Life circumstances** — Job loss, relocation, health issues, family emergency. The client needs to stop, and the reason has nothing to do with coaching quality.
- **Budget or sponsor withdrawal** — The client's employer was paying and has cut the budget, or the client's personal financial situation changed.
- **Dissatisfaction** — The client isn't getting value and wants to stop. This may come after a reassignment request was declined or not offered, or it may emerge without warning.
- **Goal achieved early** — The client feels they've accomplished what they set out to do before the engagement's scheduled end. This is actually a success, even if sessions go unused.

**Coach- or practice-initiated:**
- **Client non-engagement** — The client has gone silent: multiple missed sessions, unreturned messages, no scheduling activity. At some point, the practice needs to formally acknowledge the disengagement rather than leaving the record open indefinitely.
- **Scope beyond coaching** — During sessions, the coach determines that the client's primary needs are outside the scope of coaching (clinical mental health, legal counsel, career placement). The coach recommends an appropriate referral and concludes the coaching engagement.
- **Boundary violation** — The client behaves in a way that violates the coaching agreement or professional boundaries. Rare but real.

### 9.2 The Exit Process

Regardless of the reason, a mid-engagement exit follows a structured process:

1. **Conversation** — The coach (or practice lead, depending on who's managing the situation) has an honest conversation with the client. The goal is to understand the reason, explore whether an adjustment could address the issue (pausing instead of stopping, changing cadence, switching coaches), and respect the client's decision.

2. **Formal conclusion** — If the client is exiting, the coach records a closing summary:
   - Where the client was in their engagement (sessions completed, goals progress).
   - Reason for early exit.
   - Any recommendations for the client's continued development.
   - Whether the engagement is closed permanently or paused with an expected return timeframe.

3. **Financial resolution** — The practice lead handles any billing implications per the refund and cancellation policy:
   - If the client has prepaid unused sessions, determine the refund amount based on policy (full, prorated, none — depending on the terms and the situation). If the reason is sympathetic (health crisis, employer funding withdrawal), consider being flexible even if the policy technically allows no refund. Short-term revenue from withheld fees is never worth the long-term cost of a client who feels taken advantage of.
   - Process any refund, update the enrollment record, and send the client a final statement.

4. **Portal access** — The client's portal access remains active for a defined period after exit (e.g., 30 days) so they can download session notes, receipts, and records. After that, the account transitions to inactive status. It is not deleted — the client can reactivate if they return.

5. **Follow-up** — For clients who exit on good terms (life circumstances, budget, early goal achievement), the practice lead sends a brief note 30–60 days later: "We hope things are going well. We're here whenever you're ready to continue." This keeps the relationship alive without being pushy.

### 9.3 Handling Silent Disengagement

This is the most common and most corrosive form of exit. The client simply stops booking sessions, stops responding to messages, and fades away. Left unaddressed, it wastes capacity, creates ambiguity, and can leave the client feeling guilty or awkward about returning later.

The process for managing silent disengagement:

1. **Coach outreach** (after 1 missed session or 2 weeks without scheduling) — "I noticed we don't have our next session on the calendar. Everything okay? I want to make sure we keep our momentum."
2. **Second outreach** (after 2 missed sessions or 4 weeks) — A slightly more direct message: "I haven't heard from you in a few weeks and want to check in. If things have changed, that's completely fine — just let me know so we can figure out the best path forward."
3. **Practice lead outreach** (after 6 weeks with no response) — The practice lead contacts the client directly: "I noticed your coaching sessions have paused. I want to make sure everything is okay and see if there's anything we can do. If now isn't the right time, we completely understand — your spot is here whenever you're ready."
4. **Formal pause** (after 8 weeks with no response) — The practice lead formally pauses the engagement. The system marks the enrollment as paused, stops counting sessions against any package validity clock, and records the pause with a note. The client is sent a final message: "We've paused your engagement for now. There's no pressure to continue — and when you're ready, all you need to do is reach out."

> **Best practice:** Never just close a silent client's record without reaching out. Always give the client multiple opportunities to respond before formalizing the exit. And never make the outreach punitive or guilt-inducing — the goal is to understand and help, not to collect. Many silent clients return months later when circumstances change. How you treated them during the silence determines whether they come back.

---

## 10. Inquiry & Lead Management

Not every interested person goes straight to scheduling a discovery call. Some send a message from a coach's profile page, fill out a contact form, or email the practice with questions. These inquiries are the "other front door" — less structured than the discovery call flow, but equally important to handle well. An unanswered inquiry is a lost opportunity.

### 10.1 How Inquiries Arrive

Inquiries come through several channels:

- **"Send a Message" on coach profiles** — A prospect finds a coach whose profile resonates and sends a direct message through the platform. These are often the warmest leads — the prospect has already identified a coach they're interested in.
- **General contact form** — A prospect uses the site's general contact form to ask about services, pricing, or whether coaching is right for them. These inquiries are less specific but still represent genuine interest.
- **Email to the practice** — Some prospects prefer to email directly rather than fill out forms. These should route into the same management process as other inquiries.
- **Referral introductions** — A current client, partner, or colleague sends an introduction or recommendation. These come in various formats but should be captured and tracked.

### 10.2 Triage and Response

Every inquiry gets a response. The practice lead manages the inquiry pipeline:

1. **Initial acknowledgment** — Within the same business day, the prospect receives a response acknowledging their message. This can be automated ("Thank you for reaching out — we'll get back to you within 24 hours") or personal, but it should happen quickly. The number one complaint about professional services firms is "they never got back to me."

2. **Assess the inquiry** — The practice lead reviews the message and determines what the prospect needs:
   - **Ready for a discovery call** — The prospect is clearly interested and just needs a nudge. The response includes a link to schedule a discovery call.
   - **Needs more information** — The prospect has questions about the practice, services, coaching approach, or pricing. The response answers their questions and offers a discovery call as a next step.
   - **Coach-specific interest** — The prospect messaged a specific coach and wants to know more about working with them. The response provides additional context and offers to connect them for a conversation.
   - **Not a fit / spam** — The inquiry isn't relevant. Close it politely or archive it.

3. **Respond** — The practice lead sends a personal response. Not a template blast — a thoughtful reply that addresses what the prospect actually asked.

4. **Track the outcome** — Every inquiry has a status:
   - **New** — Just received, not yet reviewed.
   - **Responded** — Reply sent, waiting for the prospect to take the next step.
   - **Converted** — Prospect scheduled a discovery call or became a client. The inquiry was successful.
   - **Closed** — Prospect didn't respond to follow-up, or the inquiry was not relevant.

### 10.3 Inquiry-to-Discovery-Call Conversion

The goal of inquiry management is simple: convert interested prospects into scheduled discovery calls. The inquiry response should make this as easy as possible:

- **Include a direct scheduling link** — Every substantive response should include a link to schedule a discovery call. Don't make the prospect navigate the site to find it.
- **Lower the barrier** — "I'd love to learn more about what you're looking for. Would a 30-minute call work? Here are some available times." Not: "Please visit our website to learn about our program options."
- **Follow up on non-responses** — If the prospect doesn't respond within a few days, send one follow-up: "Just checking in on my note from [date]. Happy to chat whenever it's convenient." One follow-up, not three. Respectful persistence, not nagging.

> **Best practice:** Measure inquiry response time. If the average time from inquiry received to first response is more than 24 hours, the practice is leaving money on the table. Speed of response is one of the strongest predictors of conversion in professional services. The prospect is motivated right now — catch them while they're interested.

### 10.4 Inquiry-Level Analytics

The practice lead should monitor inquiry patterns to understand how prospects find and engage with the practice:

- **Volume** — How many inquiries per week/month? Is it growing?
- **Source** — Which channels generate the most inquiries? Coach profiles? Contact form? Referrals?
- **Conversion rate** — What percentage of inquiries convert to discovery calls? What percentage of those convert to clients?
- **Response time** — How quickly are inquiries answered? Where are the delays?
- **Common questions** — What do prospects ask about most often? If the same question appears repeatedly, the answer should be on the website.

---

## 11. Practice Lead Operational Rhythm

The practice lead's work is woven throughout every section of this document. But without a dedicated view of their operating rhythm, the role risks becoming purely reactive — putting out fires instead of running a practice. This section defines the regular cadence of activities that keep the practice healthy, growing, and delivering consistent quality.

### 11.1 Daily

Every business day, the practice lead should:

- **Check the discovery call pipeline** — Are there new bookings? Calls approaching that need preparation? Outcomes that haven't been recorded? Follow-ups that are due? The pipeline is the practice's front door — it shouldn't be left unattended.
- **Review inquiries** — Any new messages or contact form submissions? Time-sensitive responses needed? Same-day acknowledgment is the standard.
- **Scan for urgent items** — Client escalations, coach questions, payment failures, or anything that needs attention before end of day.

This daily check takes 15–20 minutes. It's not about doing everything — it's about knowing what needs attention today.

### 11.2 Weekly

Once a week, the practice lead conducts a more thorough review:

- **Coach check-ins** — A brief conversation with each active coach (15 minutes each). How are their clients doing? Any concerns, questions, or situations they want to discuss? Any capacity changes coming? This is the single most important recurring activity for maintaining coaching quality. It catches problems early, gives coaches a sounding board, and keeps the practice lead informed without micromanaging.
- **Client health review** — Scan the active client roster for warning signals: clients who haven't scheduled their next session, clients with multiple cancellations, engagements nearing completion without a next-step conversation. Proactive attention prevents silent disengagement.
- **Session note compliance** — Are coaches documenting their sessions? The practice lead checks for sessions without notes and follows up. This is a quality and risk management issue.
- **Pipeline review** — Where are prospects in the funnel? How many discovery calls this week? How many pending outcomes? What's the conversion rate looking like?

### 11.3 Monthly

Monthly reviews are about the business, not individual transactions:

- **Financial review** — Revenue this month vs. last month vs. same month last year. Revenue by service type, by coach, by client. Outstanding invoices. Upcoming renewals and expirations. The practice lead should know the financial health of the practice without having to dig for it.
- **Service catalog review** — Are the current offerings still the right ones? Are any services consistently underperforming (low enrollment, low completion)? Should pricing be adjusted? Are there gaps in the catalog that client feedback suggests?
- **Capacity planning** — Current coach utilization across the practice. Are any coaches underutilized? Are any approaching capacity? Is the current team sufficient for expected demand, or is it time to recruit?
- **Client feedback themes** — What patterns are emerging from post-engagement feedback, reassignment requests, or exit reasons? Is there a systemic issue that needs attention?

### 11.4 Quarterly

Quarterly reviews are strategic:

- **Practice performance review** — Key metrics across the quarter: total clients served, new clients acquired, client retention rate, average engagement length, revenue growth, discovery call conversion rate, coach utilization. Compare against previous quarters and against goals.
- **Coach development conversations** — A more substantive conversation with each coach (30–60 minutes): How are they feeling about their work? What's challenging? Where do they want to grow? Are there services they'd like to deliver that they're not currently assigned to? Professional development is what keeps good coaches with the practice.
- **Strategic planning** — Based on the data and conversations: What should the practice focus on next quarter? New service development? Marketing investment? Coach recruitment? Client retention initiatives? Technology improvements?
- **Goal setting** — Set 2–3 measurable goals for the next quarter. Not aspirational wish lists — specific, trackable targets that the practice lead will review at the end of the quarter.

> **Best practice:** The operational rhythm only works if it's actually followed. Block time on the calendar for these activities — they won't happen "when you get to it." The daily check becomes a morning habit. The weekly reviews get a recurring calendar slot. The monthly and quarterly reviews are meetings the practice lead holds with themselves, protected from interruption.

### 11.5 Practice Lead Dashboard — What to Monitor

The system should surface these metrics so the practice lead doesn't have to manually assemble them:

| Category | Key Metrics |
|---|---|
| **Pipeline** | Discovery calls scheduled this week, pending outcomes, conversion rate (30-day rolling), inquiry volume and response time |
| **Clients** | Total active clients, new enrollments this month, clients approaching program completion, clients with warning signals |
| **Coaches** | Utilization rate per coach, sessions delivered this week, session notes compliance, capacity remaining |
| **Revenue** | Monthly revenue, revenue by service type, outstanding invoices, upcoming renewals |
| **Quality** | Client feedback scores, reassignment frequency, cancellation/no-show rates, average time to first session after onboarding |

---

## 12. Coach Performance & Development

Coaching quality is the product. Everything else — marketing, technology, operations — is infrastructure to deliver and support good coaching. The practice lead's most important long-term responsibility is ensuring coaches are effective, growing, and aligned with the practice's standards.

### 12.1 What Good Looks Like

Before evaluating performance, the practice needs a shared understanding of what it expects from coaches. These standards should be explicit, communicated during onboarding, and revisited regularly:

- **Session delivery** — Sessions happen on schedule. The coach is prepared. The session follows a productive structure. The client leaves with clarity and action items.
- **Documentation** — Session notes recorded same-day. Notes are substantive enough for continuity and oversight. Goals are tracked. Progress is visible.
- **Client engagement** — Clients stay engaged. Sessions are booked consistently on cadence. Cancellation and no-show rates are low. Clients re-enroll or step down gracefully rather than disappearing.
- **Responsiveness** — The coach responds to client messages within 24 hours. The practice lead's questions or check-ins are addressed promptly. Discovery call outcomes are recorded same-day.
- **Professionalism** — The coach represents the practice well. Profile is current. Communication is polished. Boundaries are maintained. Confidentiality is absolute.
- **Growth** — The coach continues to develop professionally. Pursues additional training or credentials. Brings new insights back to the practice. Seeks feedback and acts on it.

### 12.2 Performance Signals — Quantitative

The system provides data that, in aggregate, tells a story about each coach's effectiveness:

- **Client retention rate** — What percentage of a coach's clients complete their engagements? What percentage re-enroll? High retention suggests clients are getting value.
- **Session cadence adherence** — Are sessions happening on the agreed cadence, or are there frequent gaps and rescheduling? Cadence consistency correlates with client satisfaction and outcomes.
- **Cancellation and no-show rate** — A coach with unusually high cancellation rates (compared to practice averages) may have scheduling issues, client engagement problems, or appointment management challenges.
- **Session notes timeliness** — Are notes being recorded same-day? Coaches who fall behind on documentation often have broader workload or engagement issues.
- **Discovery call conversion rate** (for coaches who handle discovery calls) — Are calls converting to clients at a healthy rate? Low conversion may indicate the coach needs support with the consultative conversation.
- **Reassignment requests** — How often do clients request a change from this coach? One is normal. A pattern needs investigation.
- **Time to first session** — After a client is assigned, how quickly does the first session happen? Delays suggest the coach isn't following up promptly.

> **Key principle:** No single metric defines a coach. A coach with a lower retention rate might be assigned the most challenging clients. A coach with fewer sessions might have longer, deeper engagements. Metrics provide signals — the practice lead interprets them in context.

### 12.3 Performance Signals — Qualitative

Numbers only tell part of the story. The practice lead gathers qualitative insight through:

- **Weekly check-ins** — The recurring coach conversations described in Section 11.2. Over time, these build a nuanced picture of each coach's strengths, challenges, and growth trajectory.
- **Client feedback** — Post-engagement surveys, informal feedback during check-ins, and the tone of client communications. Are clients enthusiastic, satisfied, or going through the motions?
- **Peer observation** — In practices with multiple coaches, structured peer feedback (with consent) provides perspective that the practice lead can't see. A new coach shadowing an experienced one. A coach inviting a peer to review their approach to a case (anonymized). This isn't surveillance — it's professional development.
- **Self-assessment** — Asking coaches to reflect on their own performance: "What are you most proud of this quarter? Where did you struggle? What do you want to improve?" This builds a coaching culture within the coaching practice.

### 12.4 The Performance Conversation

The practice lead holds formal performance conversations quarterly, aligned with the quarterly strategic rhythm described in Section 11.4:

- **Prepare with data** — Review the quantitative signals. Identify patterns, not outliers. Compare against practice averages and the coach's own trajectory over time.
- **Start with strengths** — What is this coach doing well? Be specific: "Your client retention is the highest on the team. Clients clearly value working with you."
- **Address areas for development** — Be direct but supportive: "I've noticed your session notes are often recorded 3–4 days after sessions. That's impacting continuity. What's getting in the way, and how can we address it?"
- **Discuss professional goals** — Where does the coach want to grow? New certifications? New service areas? Developing a specialty? The practice should invest in coach development — it's how the practice evolves.
- **Agree on actions** — 1–2 specific things the coach will work on before the next review. Concrete, not vague. "Submit session notes within 24 hours for the next quarter" not "improve documentation."

### 12.5 When Performance Issues Are Serious

Occasionally, performance problems go beyond a development conversation. The practice lead needs a clear process for serious concerns:

1. **Identify the pattern** — A single bad session or one late set of notes is not a performance issue. A repeating pattern across multiple clients or weeks is.
2. **Direct conversation** — The practice lead has an explicit conversation with the coach: "Here's what I'm seeing. Here's the impact. I need this to change. How can I help?"
3. **Action plan** — Agree on specific changes, a timeframe for improvement, and how progress will be measured. Document this.
4. **Monitor** — Track against the action plan. Increase check-in frequency. Provide support (training, reduced load, mentorship).
5. **Decision** — If improvement happens, acknowledge it and return to normal operations. If it doesn't, the practice lead makes the difficult decision to part ways with the coach. When this happens:
   - Active clients are reassigned using the transition process described in Section 8.
   - The departing coach's access is revoked after a clean handoff.
   - The separation is handled professionally and without drama. The coaching community is small; reputation matters.

> **Best practice:** Don't delay difficult performance conversations. Waiting makes problems worse, affects clients, and ultimately makes the conversation harder. Early, direct, supportive feedback is always better than a crisis intervention months later. A practice that avoids hard conversations is not protecting people — it's putting clients at risk.