import pandas as pd
import time
from datasets import load_dataset

DOWNLOADED = {}
FAILED = []

# === 1. SpamAssassin ===
print("=" * 60)
print("1/5 Downloading SpamAssassin (bvk/SpamAssassin-spam)...")
print("=" * 60)
t0 = time.time()
try:
    ds_sa = load_dataset('bvk/SpamAssassin-spam', split='train')
    df_sa = ds_sa.to_pandas()
    df_sa['source'] = 'spamassassin'
    df_sa.to_csv('spamassassin.csv', index=False)
    DOWNLOADED['spamassassin'] = len(df_sa)
    print("  OK: %d rows (%.1fs)" % (len(df_sa), time.time()-t0))
except Exception as e:
    print("  FAILED: %s" % str(e)[:200])
    FAILED.append('spamassassin')

# === 2. Phishing Dataset (Liu) ===
print("\n" + "=" * 60)
print("2/5 Downloading Phishing Dataset (Liu)...")
print("=" * 60)
t0 = time.time()
try:
    ds_liu = load_dataset('zefang-liu/phishing-email-dataset', split='train')
    df_liu = ds_liu.to_pandas()
    df_liu['source'] = 'phishing_liu'
    df_liu.to_csv('phishing_liu.csv', index=False)
    DOWNLOADED['phishing_liu'] = len(df_liu)
    print("  OK: %d rows (%.1fs)" % (len(df_liu), time.time()-t0))
except Exception as e:
    print("  FAILED: %s" % str(e)[:200])
    FAILED.append('phishing_liu')

# === 3. Phishing 7-Dataset ===
print("\n" + "=" * 60)
print("3/5 Downloading Phishing 7-Dataset...")
print("=" * 60)
t0 = time.time()
try:
    ds_7ds = load_dataset('puyang2025/seven-phishing-email-datasets', split='train')
    df_7ds = ds_7ds.to_pandas()
    df_7ds['source'] = 'phishing_7ds'
    df_7ds.to_csv('phishing_7ds.csv', index=False)
    DOWNLOADED['phishing_7ds'] = len(df_7ds)
    print("  OK: %d rows (%.1fs)" % (len(df_7ds), time.time()-t0))
except Exception as e:
    print("  FAILED: %s" % str(e)[:200])
    FAILED.append('phishing_7ds')

# === 4. Phishing v2.0 ===
print("\n" + "=" * 60)
print("4/5 Downloading Phishing v2.0...")
print("=" * 60)
t0 = time.time()
try:
    ds_v2 = load_dataset('cybersectony/PhishingEmailDetectionv2.0', split='train')
    df_v2 = ds_v2.to_pandas()
    df_v2['source'] = 'phishing_v2'
    df_v2.to_csv('phishing_v2.csv', index=False)
    DOWNLOADED['phishing_v2'] = len(df_v2)
    print("  OK: %d rows (%.1fs)" % (len(df_v2), time.time()-t0))
except Exception as e:
    print("  FAILED: %s" % str(e)[:200])
    FAILED.append('phishing_v2')

# === 5. Phishing emails (Rabin) ===
print("\n" + "=" * 60)
print("5/5 Downloading Phishing emails (Rabin)...")
print("=" * 60)
t0 = time.time()
try:
    ds_rbn = load_dataset('drorrabin/phishing_emails-data', split='train')
    df_rbn = ds_rbn.to_pandas()
    df_rbn['source'] = 'phishing_rbn'
    df_rbn.to_csv('phishing_rbn.csv', index=False)
    DOWNLOADED['phishing_rbn'] = len(df_rbn)
    print("  OK: %d rows (%.1fs)" % (len(df_rbn), time.time()-t0))
except Exception as e:
    print("  FAILED: %s" % str(e)[:200])
    FAILED.append('phishing_rbn')

# === Summary ===
print("\n" + "=" * 60)
print("DOWNLOAD SUMMARY")
print("=" * 60)
for name, count in DOWNLOADED.items():
    print("  [OK] %s: %d rows" % (name, count))
if FAILED:
    for name in FAILED:
        print("  [FAIL] %s" % name)
total = sum(DOWNLOADED.values())
print("  ---")
print("  Total new rows: %d" % total)
print("  Successful: %d/5" % len(DOWNLOADED))
