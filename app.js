"use strict";
document.getElementById('print-cv').addEventListener('click', () => window.print());

const email = 'letienphatwork@gmail.com';
const copyButton = document.getElementById('copy-email');
copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  const status = document.getElementById('copy-status');
  try {
    await navigator.clipboard.writeText(email);
    status.textContent = 'Email copied. Ready to paste.';
  } catch {
    status.textContent = 'Please select and copy the email address above.';
  }
});

const lab = document.querySelector('.signal-lab');
const faultButton = document.getElementById('toggle-fault');
let hasFault = false;
function signalPath(fault) {
  return Array.from({length: 201}, (_, i) => {
    const x = i * 3;
    const spike = fault ? 55 * Math.exp(-Math.pow((x - 354) / 13, 2)) : 0;
    const y = 80 - 25 * Math.sin(x / 22) - spike;
    return `${i ? 'L' : 'M'}${x},${y.toFixed(2)}`;
  }).join(' ');
}
document.getElementById('expected-signal').setAttribute('d', signalPath(false));
document.getElementById('observed-signal').setAttribute('d', signalPath(false));
lab.hidden = false;
faultButton.addEventListener('click', () => {
  hasFault = !hasFault;
  lab.classList.toggle('has-fault', hasFault);
  faultButton.setAttribute('aria-pressed', String(hasFault));
  faultButton.textContent = hasFault ? 'Reset signal' : 'Inject a fault';
  document.getElementById('observed-signal').setAttribute('d', signalPath(hasFault));
  document.getElementById('signal-status').textContent = hasFault ? 'Fault injected: sudden spike' : 'Normal signal';
  document.getElementById('signal-description').textContent = hasFault
    ? 'The observed waveform has a sudden spike that departs from the dashed expected pattern.'
    : 'A regular waveform following the expected pattern.';
});
